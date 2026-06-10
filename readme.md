# ✨ Nexus CV Tailor

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Powered by Gemini](https://img.shields.io/badge/Powered%20by-Gemini%202.5%20Flash-orange.svg)](https://deepmind.google/technologies/gemini/)


**Nexus CV Tailor** is an advanced, multi-agent AI pipeline designed to instantly tailor resumes and generate professional cover letters matching any target job description. Powered by Gemini 2.5 Flash, it features a dual-manager adversarial loop, automated verification auditing, semantic project retrieval (RAG), and a humanizer to produce recruiter-approved, ATS-friendly documents that sound genuinely human.

---

## 💡 How It Makes Your Life Easier & Solves Daily Problems

Applying for jobs in the modern market is a challenging, time-consuming process. Nexus CV Tailor solves the most common frustrations faced by job seekers:

### 1. The Multi-Hour Tailoring Fatigue
* **The Daily Problem:** Manually adjusting your resume, tweaking bullet points, and rewriting cover letters for 5 to 10 different job postings per day takes hours. Most job seekers end up sending generic applications, resulting in low response rates.
* **How Nexus Solves It:** By pasting a target job description and launching the pipeline, Nexus automatically reframes your professional summary, selects the most relevant technical skills, and aligns your experience highlights in **15 to 30 seconds**.

### 2. The AI-Written Detection Trap
* **The Daily Problem:** Standard LLM generators output formulaic, overly polite, or corporate-sounding documents containing giveaway AI expressions (*"in today's fast-paced world"*, *"testament to my skills"*). Recruiters and ATS systems increasingly flag or filter out these generic AI-generated files.
* **How Nexus Solves It:** It features dedicated **Humanizer** and **Anti-AI Guard** agents that strip away AI tells, improve flow, and adjust readability. It even injects subtle, natural imperfections and soft styling rules to ensure your application passes stringent AI checks while maintaining professional tone.

### 3. The Hallucination Danger (Honesty & Verification)
* **The Daily Problem:** Generative AI tools frequently invent credentials, alter employment dates, or fabricate past projects just to match a job description. Presenting these inaccuracies in an interview can destroy your credibility.
* **How Nexus Solves It:** The pipeline includes a strict **Verification Audit Agent**. It cross-references every generated CV bullet and experience section against your immutable profile (`my_profile.json`). Any attempt by the model to hallucinate details or alter factual history is flagged, corrected, and brought back to reality.

### 4. The Portfolio Selection Dilemma
* **The Daily Problem:** You have a vast list of past projects, codebases, and achievements, but you don't know which ones are most relevant to highlight for a specific role.
* **How Nexus Solves It:** You can upload markdown (`.md`) or PDF portfolio files to your workspace's Data Vault. The app uses semantic search (**Gemini Embeddings + Cosine Similarity**) to dynamically pull in only the top-5 most relevant projects matching the job description to use as context for tailoring.

### 5. Formatting & Layout Nightmares
* **The Daily Problem:** Getting margins right, formatting cover letters to specific regional standards (such as the rigid **German DIN 5008 layout**), and exporting clean, page-bounded PDFs from web tools is a constant struggle.
* **How Nexus Solves It:** Nexus integrates tailored CSS layouts and compiling agents. It automatically structures cover letters to match **DIN 5008** specifications and uses WeasyPrint to export print-ready, pixel-perfect A4 PDF files.

---

## 🛠️ Key Features

- **ATS Analyst Agent:** Dissects job descriptions for core focus areas, target responsibilities, and key terminology.
- **Verification & Compliance:** Hard-coded check against your local profile database prevents AI hallucination.
- **RAG-Powered Data Vault:** Semantic search fetches the most relevant project information from your uploaded files.
- **Dual-Manager Adversarial Loop:**
  - **Quality Manager:** Assesses keyword density, role focus alignment, and impact.
  - **Anti-AI Guard:** Audits for robotic language, syntax patterns, and structure flow.
  - Documents cycle through a revision loop until approved by both managers.
- **Direct PDF Export:** Compiles HTML and custom print CSS into downloadable PDFs.

---

## ⚙️ Multi-Agent Architecture

```mermaid
graph TD
    subgraph Input Stage
        JD[Job Description]
        PF[Project Portfolio Files .md / .pdf]
        Profile[Immutable Profile my_profile.json]
    end

    subgraph Analysis & Retrieval
        JD --> ATS[ATS Analyst Agent]
        ATS --> Keywords[Keywords & Role Focus]
        PF --> RAG[RAG Semantic Retrieval]
        RAG --> VaultData[Top 5 Relevant Projects]
    end

    subgraph Tailoring & Verification
        Keywords & VaultData & Profile --> Tailor[Resume Tailor Agent]
        Tailor --> TailorJSON[Tailored CV JSON]
        TailorJSON --> Audit[Verification Audit Agent]
        Profile --> Audit
        Audit --> AuditedCV[Verified CV JSON]
    end

    subgraph Generation & Styling
        Keywords & VaultData & Profile --> CoverArch[Cover Architect Agent]
        CoverArch --> CoverJSON[Cover Letter JSON]
        AuditedCV & CoverJSON --> Compiler[Markdown Compilers]
    end

    subgraph Refining Loop (Max 3 Loops)
        Compiler --> RawMD[Raw Markdown Documents]
        RawMD --> Humanizer[Humanization Agents]
        Humanizer --> HumMD[Humanized Documents]
        HumMD --> MgrA[Quality Manager Agent]
        HumMD --> MgrB[Anti-AI Guard Agent]
        
        MgrA & MgrB --> Approved{Approved?}
        Approved -- No / Critiques --> Revise[Revision Agent]
        Revise --> Humanizer
    end

    subgraph Final Compilation
        Approved -- Yes --> Final[Imperfections & Clean-up Agent]
        Final --> PDF[WeasyPrint PDF Engines]
        PDF --> Downloads[Tailored CV & DIN 5008 Cover Letter PDFs]
    end

    style ATS fill:#f9f,stroke:#333,stroke-width:2px
    style Audit fill:#ff9,stroke:#333,stroke-width:2px
    style MgrA fill:#9f9,stroke:#333,stroke-width:2px
    style MgrB fill:#9f9,stroke:#333,stroke-width:2px
    style Approved fill:#ffcc00,stroke:#333,stroke-width:2px
```

---

## 📂 Project Structure

```bash
cv_agent/
│
├── agents/                       # Specialized AI agents
│   ├── ats.py                    # Analyzes job description keywords
│   ├── resume_tailor.py          # Customizes resume bullet points
│   ├── cover_architect.py        # Designs cover letter structure
│   ├── verification_audit.py     # Hard-crosschecks facts to prevent hallucinations
│   ├── humanizer.py              # Softens tone, replaces robotic syntax
│   ├── quality_manager.py        # Quality assurance manager agent
│   ├── anti_ai_guard.py          # Checks for AI writing style patterns
│   ├── revision.py               # Re-writes based on loop critiques
│   ├── compiler.py               # Renders CV JSON to markdown
│   ├── cover_compiler.py         # Renders Cover JSON to markdown
│   └── imperfections.py          # Adds subtle human-like formatting details
│
├── data/
│   └── my_profile.json           # Your immutable personal/career data
│
├── rules/                        # Formatting and regional regulations
│   ├── humanize_rules.md         # Text styling rules to reduce AI score
│   ├── language_rules.md         # Tone and voice guidelines
│   ├── layout_rules.md           # Structural layout requirements
│   └── market_germany.md         # German application style constraints
│
├── app.py                        # Streamlit web user interface
├── orchestrator.py               # Orchestrates multi-agent execution
├── shared.py                     # File processing, embeddings, schemas
├── .env                          # Local environment secrets
└── readme.md                     # Documentation
```

---

## 🚀 Getting Started

### 📋 Prerequisites

To export high-quality PDF files, this application utilizes **WeasyPrint**, which requires system-level packages for PDF and image rendering. Install the system dependencies according to your OS:

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
```

#### macOS (using Homebrew)
```bash
brew install pango cairo libffi
```

#### Windows
Please follow the [official WeasyPrint Windows installation guide](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows).

---

### 💻 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cv_agent.git
   cd cv_agent
   ```

2. **Set up a virtual environment and activate it:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install streamlit google-genai weasyprint markdown numpy pypdf
   ```

4. **Set up your API Key:**
   Create a `.env` file in the root directory and add your Gemini API Key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

---

## ⚙️ Configuration & Usage

### 1. Update Your Core Profile
Before running the application, make sure to update `data/my_profile.json` with your real profile, experiences, and educational facts. This file is used as the **source of truth** by the auditor agent.

### 2. Add Project Vault Files (Optional)
If you want to use the RAG feature, gather details of your projects in Markdown (`.md`) or PDF formats. You can upload them dynamically in the Streamlit sidebar.

### 3. Launch the Application
Run the Streamlit server:
```bash
streamlit run app.py
```

### 4. Run the Pipeline
1. Open the local address (typically `http://localhost:8501`).
2. Paste the target job description.
3. Upload any project files you want to match against the description.
4. Click **🚀 Generate CV & Cover Letter**.
5. Preview the documents in the tabs and download the tailored PDF files.

---

## 🛡️ License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
