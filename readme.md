# Nexus CV Tailor – Multi-Agent CV & Cover Letter Generator

**Powered by Gemini 2.5 Flash** – produces tailored, human‑sounding, recruiter‑approved documents.

## Features
- 6+ specialised agents (ATS, Resume Tailor, Cover Architect, Humanizer, Quality Manager, Anti‑AI Guard)
- Dual‑manager adversarial loop (reduces AI detection)
- German DIN 5008 cover letter format
- Upload your project files (.md / .pdf)
- Download tailored CV and cover letter as separate PDFs

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set `GEMINI_API_KEY` in environment or `.env`
3. Run: `streamlit run app.py`

## Folder structure
- `agents/` – each agent in its own file
- `orchestrator.py` – main pipeline
- `shared.py` – utilities, schemas, embeddings
- `data/my_profile.json` – your immutable facts
- `rules/*.md` – style and market guidelines