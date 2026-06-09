# agents/quality_manager.py
from shared import load_rule_files
from agents import ask_gemini_json
from google.genai import types


critique_schema = types.Schema(
    type=types.Type.OBJECT,
    properties={
        "approved": types.Schema(type=types.Type.BOOLEAN),
        "critique": types.Schema(type=types.Type.STRING)
    },
    required=["approved", "critique"]
)

def quality_manager(client, cv_md, cover_md, keywords, role_focus):
    rules = load_rule_files()
    prompt = f"""
You are a Quality & Alignment Manager. Output JSON: {{"approved": bool, "critique": "list of issues or empty"}}
Check:
- All keywords appear naturally: {keywords}
- No grammar errors or sentence fragments.
- Cover letter has salutation and closing.
- Resume bullets are impactful.

**HONESTY RULE:**
- Never claim a skill, project, or achievement that is not present in the profile or project vault.
- Do not exaggerate metrics or invent results.
- If you lack a required qualification, focus on transferable skills instead of lying.

Resume:
{cv_md}

Cover letter:
{cover_md}

Role focus: {role_focus}
"""
    return ask_gemini_json(client, prompt, critique_schema, temperature=0.1)