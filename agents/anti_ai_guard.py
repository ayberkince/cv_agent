# agents/anti_ai_guard.py
from agents import ask_gemini_json
from google.genai import types
from shared import load_rule_files

def anti_ai_guard(client, cv_md, cover_md):
    rules = load_rule_files()
    prompt = f"""
You are an adversarial AI detector. Output JSON: {{"approved": bool, "critique": "list of AI-like patterns or empty"}}
Flag:
- Repeated sentence openings (e.g., every bullet "Engineered...")
- Perfect parallelism
- No sentence fragments
- No colloquialisms
- Over‑optimised X‑Y‑Z phrases

**HONESTY RULE:**
- Never claim a skill, project, or achievement that is not present in the profile or project vault.
- Do not exaggerate metrics or invent results.
- If you lack a required qualification, focus on transferable skills instead of lying.

Resume:
{cv_md}

Cover letter:
{cover_md}
"""
    schema = types.Schema(
        type=types.Type.OBJECT,
        properties={
            "approved": types.Schema(type=types.Type.BOOLEAN),
            "critique": types.Schema(type=types.Type.STRING)
        },
        required=["approved", "critique"]
    )
    return ask_gemini_json(client, prompt, schema, temperature=0.1)