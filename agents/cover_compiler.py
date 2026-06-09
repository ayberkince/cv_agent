# agents/cover_compiler.py
from datetime import datetime
import json

def compile_cover(cover_data: dict) -> str:
    with open("data/my_profile.json") as f:
        profile = json.load(f)
    pi = profile["personal_info"]
    # German date format: DD.MM.YYYY
    current_date = datetime.now().strftime("%d.%m.%Y")

    # Sender address block (your details)
    sender = f"{pi['name']}\n{pi['location']}\n{pi['phone']}\n{pi['email']}"

    # Recipient block – placeholder; user can edit manually after generation
    recipient = ""

    # Build Markdown with HTML divs for styling
    md = f"""
<div class="sender-address">{sender}</div>

<div class="recipient-address">{recipient}</div>

<div class="date">{current_date}</div>

<div class="subject-line">{cover_data['subject_line']}</div>

{cover_data['salutation']}

"""
    for para in cover_data['body_paragraphs']:
        md += f"{para}\n\n"
    md += f"{cover_data['closing_paragraph']}\n\n"
    md += f"{cover_data['signature']}\n"
    return md