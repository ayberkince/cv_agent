# agents/imperfections.py
from agents import ask_gemini_json
import random

def add_imperfections(text: str) -> str:
    lines = text.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        if line.strip().startswith('- ') and i % 5 == 0:
            line = line.rstrip('.')
        new_lines.append(line)
    return '\n'.join(new_lines)

def clean_cv_output(text: str) -> str:
    if text.startswith("```markdown"):
        text = text[len("```markdown"):]
    if text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    lines = text.split('\n')
    lines = [l for l in lines if not l.strip().startswith(("Here is", "I have", "This CV", "```"))]
    return '\n'.join(lines).strip()