# agents/__init__.py
from google import genai
from google.genai import types
import json

def ask_gemini_json(client: genai.Client, prompt: str, response_schema=None, temperature=0.2):
    """Helper to call Gemini with JSON response format."""
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        temperature=temperature
    )
    if response_schema:
        config.response_schema = response_schema
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config
    )
    return json.loads(response.text)