# agents/cover_architect.py
from shared import load_rule_files
from agents import ask_gemini_json
from google.genai import types
import json

cover_schema = types.Schema(
    type=types.Type.OBJECT,
    properties={
        "salutation": types.Schema(type=types.Type.STRING),
        "subject_line": types.Schema(type=types.Type.STRING),
        "opening_paragraph": types.Schema(type=types.Type.STRING),
        "body_paragraphs": types.Schema(type=types.Type.ARRAY, items=types.Schema(type=types.Type.STRING)),
        "closing_paragraph": types.Schema(type=types.Type.STRING),
        "signature": types.Schema(type=types.Type.STRING)
    },
    required=["salutation", "subject_line", "opening_paragraph", "body_paragraphs", "closing_paragraph", "signature"]
)

def cover_architect(client, jd_text, profile_json, vault_data):
    rules = load_rule_files()
    prompt = f"""
Write a cover letter with **complete sentences only**. Use first person ("I").
Output JSON with fields: salutation, opening_paragraph, body_paragraphs (array), closing_paragraph, signature.

**HONESTY RULE:**
- Never claim a skill, project, or achievement that is not present in the profile or project vault.
- Do not exaggerate metrics or invent results.
- If you lack a required qualification, focus on transferable skills instead of lying.

Profile:
{json.dumps(profile_json, indent=2)}

Project highlights:
{vault_data}

Job description:
{jd_text}
"""
    return ask_gemini_json(client, prompt, cover_schema, temperature=0.2)