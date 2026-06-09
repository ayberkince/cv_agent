# agents/humanizer.py
from google import genai
from google.genai import types
from agents import ask_gemini_json
from shared import load_rule_files

def humanize_text(client: genai.Client, markdown_text: str) -> str:
    rules = load_rule_files()
    prompt = f"""
You are an expert editor. Rewrite the resume below to sound 100% human-written.
Follow these rules exactly:

1. DELETE every "I", "me", "my", "we", "us", "I'm", "I've". Use no first-person.
2. Break at least 30% of the sentences into fragments (2-5 words, no verb).
3. Remove the period from 1-2 bullets per section.
4. Replace 2-3 perfect commas with dashes or line breaks.
5. Change one perfect bullet into a short phrase like "Team lead for 50+." or "Dashboard in Streamlit."
6. Use one mild colloquialism: "a ton of", "handful of", "on the fly", "plugged into".
7. Do NOT change any facts, numbers, dates, or project names.

Resume text:
{markdown_text}

Output only the revised Markdown.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(temperature=0.7)
    )
    return response.text