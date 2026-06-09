# orchestrator.py
from google import genai
from agents.ats import ats_analyst
from agents.resume_tailor import resume_tailor
from agents.cover_architect import cover_architect
from agents.verification_audit import verification_audit
from agents.compiler import compile_cv
from agents.cover_compiler import compile_cover
from agents.humanizer import humanize_text
from agents.cover_humanizer import humanize_cover_letter
from agents.imperfections import add_imperfections, clean_cv_output
from agents.quality_manager import quality_manager
from agents.anti_ai_guard import anti_ai_guard
from agents.revision import revise_document
from shared import process_uploaded_files, cosine_similarity, get_embedding
import json

def run_full_pipeline(jd_text, api_key, project_files, profile_path="data/my_profile.json", max_loops=3):
    client = genai.Client(api_key=api_key)

    # ----- 1. ATS -----
    ats = ats_analyst(client, jd_text)
    keywords = ats["keywords"]
    role_focus = ats["role_focus"]

    # ----- 2. Project retrieval (same as your current code) -----
    project_contents, project_embeddings = process_uploaded_files(client, project_files)
    jd_embedding = get_embedding(client, jd_text)
    scores = []
    for pid, emb in project_embeddings.items():
        scores.append((pid, cosine_similarity(jd_embedding, emb)))
    scores.sort(key=lambda x: x[1], reverse=True)
    top_candidates = scores[:5]
    vault_data = "\n\n".join([f"## {pid}\n{project_contents[pid]}" for pid, _ in top_candidates])

    # ----- 3. Load immutable profile -----
    with open(profile_path, "r") as f:
        profile_json = json.load(f)

    # ----- 4. Generate CV (structured JSON) & compile to Markdown -----
    tailored_cv_json = resume_tailor(client, jd_text, profile_json, vault_data)
    audited_cv_json = verification_audit(client, tailored_cv_json, profile_json)
    cv_md = compile_cv(audited_cv_json)

    # ----- 5. Generate cover letter (structured JSON) & compile -----
    cover_json = cover_architect(client, jd_text, profile_json, vault_data)
    cover_md = compile_cover(cover_json)

    # ----- 6. First humanisation -----
    cv_md = humanize_text(client, cv_md)
    cover_md = humanize_cover_letter(client, cover_md)

    # ----- 7. Dual‑manager loop -----
    for loop in range(max_loops):
        mgr_a = quality_manager(client, cv_md, cover_md, keywords, role_focus)
        mgr_b = anti_ai_guard(client, cv_md, cover_md)

        approved = mgr_a["approved"] and mgr_b["approved"]
        if approved:
            print(f"✅ Loop {loop+1}: both managers approved")
            break
        else:
            # Combine critiques
            critiques = []
            if not mgr_a["approved"]:
                critiques.append(mgr_a["critique"])
            if not mgr_b["approved"]:
                critiques.append(mgr_b["critique"])
            all_issues = "\n".join(critiques)
            print(f"🔄 Loop {loop+1}: revising – issues found")
            # Revise both documents
            cv_md = revise_document(client, cv_md, all_issues, doc_type="resume")
            cover_md = revise_document(client, cover_md, all_issues, doc_type="cover letter")
            # Re‑humanise after revision
            cv_md = humanize_text(client, cv_md)
            cover_md = humanize_cover_letter(client, cover_md)

    # ----- 8. Final imperfections & cleanup -----
    cv_md = add_imperfections(cv_md)
    cover_md = add_imperfections(cover_md)   # you may want a softer version for cover
    cv_md = clean_cv_output(cv_md)
    cover_md = clean_cv_output(cover_md)

    return cv_md, cover_md