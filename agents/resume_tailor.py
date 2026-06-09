from agents import ask_gemini_json
from shared import TailoredCVDataSchema, load_rule_files
import json

def resume_tailor(client, jd_text, profile_json, vault_data):
    rules = load_rule_files()
    prompt = f"""
You are an expert resume optimizer. Output JSON matching the schema.

-- RULES --
{rules}

**HONESTY RULE (STRICTLY ENFORCED):**
- Do NOT invent any skill, metric, tool, project name, or achievement.
- Every bullet point must be directly derived from the immutable profile or the project vault.
- If the job description asks for a skill you don't have, simply omit it – never fabricate.
- Any violation makes the output invalid.

-- JOB DESCRIPTION --
{jd_text}

-- PROFILE --
{json.dumps(profile_json, indent=2)}

-- PROJECT VAULT --
{vault_data}

-- INSTRUCTIONS --
1. Professional summary.
2. Group technical skills.
3. Choose 2-3 projects, write 3-4 X‑Y‑Z bullets (no "as measured by").
4. Rewrite experience with strong verbs and metrics.
5. Do not invent facts.
6. Date format MM.YYYY – MM.YYYY.
"""
    return ask_gemini_json(client, prompt, TailoredCVDataSchema, temperature=0.3)