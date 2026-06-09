from shared import load_rule_files

def humanize_cover_letter(client, text: str) -> str:
    rules = load_rule_files()
    prompt = f"""
Make this cover letter sound human. Keep first‑person ("I").
- Vary sentence openings (not all start with "I").
- Use one mild colloquialism (e.g., "excited about", "a great fit").
- Ensure no sentence fragments.
- Do not change facts.

Text:
{text}

Output only the revised cover letter.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config={"temperature": 0.5}
    )
    return response.text