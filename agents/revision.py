# agents/revision.py
from agents import ask_gemini_json

def revise_document(client, doc_md, critique_text, doc_type="resume"):
    prompt = f"""
You are an editor. Revise the {doc_type} to fix all issues below.
Keep all facts, dates, names unchanged.
Output only the revised Markdown.

**HONESTY RULE:**
- Never claim a skill, project, or achievement that is not present in the profile or project vault.
- Do not exaggerate metrics or invent results.
- If you lack a required qualification, focus on transferable skills instead of lying.

Issues:
{critique_text}

Original {doc_type}:
{doc_md}
"""
    # No JSON schema – return plain text
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt, config={"temperature": 0.3})
    return response.text.strip()