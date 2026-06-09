# shared.py – Shared utilities, embeddings, schemas, and helpers
import os
import json
import io
from typing import List, Dict, Tuple, Any
import numpy as np
from google import genai
from google.genai import types
from pypdf import PdfReader

# ----------------------------------------------------------------------------
# Constants
# ----------------------------------------------------------------------------
EMBEDDING_MODEL = "gemini-embedding-001"   # or "gemini-embedding-001"
GENERATION_MODEL = "gemini-2.5-flash"
SIMILARITY_TOP_K = 5

# ----------------------------------------------------------------------------
# Embedding & Similarity
# ----------------------------------------------------------------------------
def cosine_similarity(vec_a: List[float], vec_b: List[float]) -> float:
    a = np.array(vec_a)
    b = np.array(vec_b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(client: genai.Client, text: str) -> List[float]:
    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text[:2000]
    )
    return response.embeddings[0].values

# ----------------------------------------------------------------------------
# Process uploaded files (extract text from MD/PDF, compute embeddings)
# ----------------------------------------------------------------------------
def process_uploaded_files(client: genai.Client, project_files: List[Tuple[str, bytes]]) -> Tuple[Dict[str, str], Dict[str, List[float]]]:
    project_contents = {}
    project_embeddings = {}
    for filename, content_bytes in project_files:
        pid = os.path.splitext(filename)[0]
        if filename.endswith('.md'):
            content = content_bytes.decode('utf-8', errors='ignore')
        elif filename.endswith('.pdf'):
            reader = PdfReader(io.BytesIO(content_bytes))
            content = "\n".join([page.extract_text() or "" for page in reader.pages])
        else:
            continue
        truncated = content[:2000]
        emb = get_embedding(client, truncated)
        project_contents[pid] = content
        project_embeddings[pid] = emb
        print(f"  - Processed {pid}")
    return project_contents, project_embeddings

# ----------------------------------------------------------------------------
# Load rule files (Markdown instructions for the LLM)
# ----------------------------------------------------------------------------
def load_rule_files() -> str:
    rules_paths = [
        "rules/layout_rules.md",
        "rules/language_rules.md",
        "rules/market_germany.md",
        "rules/humanize_rules.md"
    ]
    content = ""
    for path in rules_paths:
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                content += f"\n\n--- {os.path.basename(path)} ---\n{f.read()}"
    return content

# ----------------------------------------------------------------------------
# Gemini Structured Output Schemas (used by resume_tailor and verification_audit)
# ----------------------------------------------------------------------------
CVProjectSection = types.Schema(
    type=types.Type.OBJECT,
    properties={
        "project_name": types.Schema(type=types.Type.STRING),
        "context": types.Schema(type=types.Type.STRING),
        "dates": types.Schema(type=types.Type.STRING, description="Format: MM.YYYY – MM.YYYY"),
        "tech_stack_line": types.Schema(type=types.Type.STRING, description="Comma separated list of tech used"),
        "bullets": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(type=types.Type.STRING),
            description="3-4 impact bullets"
        )
    },
    required=["project_name", "context", "dates", "tech_stack_line", "bullets"]
)

CVExperienceSection = types.Schema(
    type=types.Type.OBJECT,
    properties={
        "role_title": types.Schema(type=types.Type.STRING),
        "company": types.Schema(type=types.Type.STRING),
        "dates": types.Schema(type=types.Type.STRING),
        "bullets": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(type=types.Type.STRING)
        )
    },
    required=["role_title", "company", "dates", "bullets"]
)

TailoredCVDataSchema = types.Schema(
    type=types.Type.OBJECT,
    properties={
        "professional_summary": types.Schema(type=types.Type.STRING),
        "technical_skills_grouped": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(type=types.Type.STRING)
        ),
        "tailored_projects": types.Schema(
            type=types.Type.ARRAY,
            items=CVProjectSection
        ),
        "tailored_experience": types.Schema(
            type=types.Type.ARRAY,
            items=CVExperienceSection
        )
    },
    required=["professional_summary", "technical_skills_grouped", "tailored_projects", "tailored_experience"]
)