# agents/ats.py
import json
from agents import ask_gemini_json
from google import genai
from google.genai import types

def ats_analyst(client: genai.Client, jd_text: str) -> dict:
    prompt = f"""
You are an ATS keyword analyst. Extract from the job description:
- role_focus (one short sentence)
- top 8 technical keywords (list)

Return ONLY JSON: {{"role_focus": "...", "keywords": [...]}}

Job description:
{jd_text}
"""
    schema = types.Schema(
        type=types.Type.OBJECT,
        properties={
            "role_focus": types.Schema(type=types.Type.STRING),
            "keywords": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING)
            )
        },
        required=["role_focus", "keywords"]
    )
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=schema,
            temperature=0.2
        )
    )
    return json.loads(response.text)