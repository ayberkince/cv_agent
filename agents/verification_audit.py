# agents/verification_audit.py
import json
from google import genai
from google.genai import types
from shared import TailoredCVDataSchema

def verification_audit(client: genai.Client, generated_cv_data: dict, profile_json: dict) -> dict:
    audit_prompt = f"""
You are a strict QA editor. Verify that the generated CV data contains no hallucinated facts, metrics, or tools.
Compare against the immutable profile.

-- GENERATED CV DATA --
{json.dumps(generated_cv_data, indent=2)}

-- IMMUTABLE PROFILE (GROUND TRUTH) --
{json.dumps(profile_json, indent=2)}

-- INSTRUCTIONS --
1. Scan every skill, project bullet, experience bullet.
2. Remove or replace any fact not present in the immutable profile.
3. Ensure no robotic phrases like "as measured by".
4. Output corrected JSON using the same schema.
5. **If any fact (e.g., a metric, a tool, a project name) is not present in the immutable profile or the project vault, DELETE it immediately. Do NOT replace it with a made‑up alternative.**
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=audit_prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=TailoredCVDataSchema,
            temperature=0.1
        )
    )
    return json.loads(response.text)