# agents/compiler.py
from datetime import datetime
import json

def compile_cv(cv_data: dict) -> str:
    with open("data/my_profile.json", "r") as f:
        profile = json.load(f)
    pi = profile["personal_info"]
    current_date = datetime.now().strftime("%B %Y")

    md = f"# {pi['name']}\n\n"
    md += f"**{pi['location']}** | {pi['phone']} | {pi['email']}\n"
    md += f"**LinkedIn:** [{pi['links']['linkedin'].split('//')[1]}]({pi['links']['linkedin']}) | "
    md += f"**GitHub:** [{pi['links']['github'].split('//')[1]}]({pi['links']['github']})\n\n"
    md += "---\n\n"

    md += "## Professional Summary\n\n"
    md += f"{cv_data['professional_summary']}\n\n---\n\n"

    md += "## Technical Skills\n\n"
    for skill_line in cv_data['technical_skills_grouped']:
        md += f"* {skill_line}\n"
    md += "\n---\n\n"

    md += "## Projects\n\n"
    for proj in cv_data['tailored_projects']:
        md += f"**{proj['project_name']}** | *{proj['context']}* | <span class=\"date\">{proj['dates']}</span>\n\n"
        md += f"*{proj['tech_stack_line']}*\n\n"
        for bullet in proj['bullets']:
            md += f"- {bullet}\n"
        md += "\n"
    md += "---\n\n"

    md += "## Experience\n\n"
    for exp in cv_data['tailored_experience']:
        md += f"**{exp['role_title']}** | *{exp['company']}* | <span class=\"date\">{exp['dates']}</span>\n\n"
        for bullet in exp['bullets']:
            md += f"- {bullet}\n"
        md += "\n"
    md += "---\n\n"

    # Education section
    md += "## Education\n\n"
    for edu in profile['education']:
        md += f"**{edu['degree']}** | *{edu['institution']}* | <span class=\"date\">{edu['start_date']} – {edu['end_date']}</span>\n\n"
        for detail in edu['details']:
            md += f"- {detail}\n"
        md += "\n"
    md += "---\n\n"

    # Language Skills
    md += "## Language Skills\n\n"
    for lang in profile['languages']:
        md += f"* {lang['language']} ({lang['level']})\n"
    md += "\n---\n\n"

    # Certifications
    if "certifications" in profile and profile["certifications"]:
        md += "## Certifications\n\n"
        for cert in profile['certifications']:
            md += f"- {cert}\n"
        md += "\n---\n\n"

    md += f"*Potsdam, {current_date}*\n"
    return md