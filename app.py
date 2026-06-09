# app.py – Streamlit UI for dual CV + Cover Letter generation
import streamlit as st
from orchestrator import run_full_pipeline
import os
import markdown
from weasyprint import HTML

st.set_page_config(page_title="Nexus CV Tailor", layout="wide")
st.title("✨ Nexus CV Tailor")
st.markdown("Transform your resume into a perfect match for any job description in seconds!")

# Sidebar
with st.sidebar:
    st.markdown("### 🔑 Authentication")
    api_key = st.text_input("Enter Gemini API Key", type="password")
    if not api_key:
        api_key = os.environ.get("GEMINI_API_KEY", "")
        if api_key:
            st.success("🔑 Using API key from environment")
        else:
            st.warning("🔑 Please enter your Gemini API key")

    st.markdown("---")
    st.markdown("### 📂 Data Vault")
    uploaded_files = st.file_uploader(
        "Upload your project files (.md / .pdf)",
        type=["md", "pdf"],
        accept_multiple_files=True
    )
    if uploaded_files:
        project_files = [(uf.name, uf.read()) for uf in uploaded_files]
        st.session_state["project_files"] = project_files
        st.success(f"🎉 {len(project_files)} files loaded")
    elif "project_files" not in st.session_state:
        st.session_state["project_files"] = []

    st.markdown("---")
    st.caption("⚡ Multi‑agent pipeline (ATS → Tailor → Cover → Humanizer → Dual Managers → Compiler)")

# Main columns
col_left, col_right = st.columns([1, 1.2], gap="large")

with col_left:
    st.markdown("### 📌 Job Description")
    jd_text = st.text_area("Paste the target job description:", height=450)
    generate = st.button("🚀 Generate CV & Cover Letter", use_container_width=True)

with col_right:
    st.markdown("### 📄 Generated Documents")
    if generate and jd_text and api_key:
        if not st.session_state["project_files"]:
            st.warning("Please upload at least one project file.")
        else:
            with st.spinner("Running multi‑agent pipeline (15‑30 seconds)..."):
                try:
                    cv_md, cover_md = run_full_pipeline(
                        jd_text=jd_text,
                        api_key=api_key,
                        project_files=st.session_state["project_files"]
                    )
                    st.session_state["cv_md"] = cv_md
                    st.session_state["cover_md"] = cover_md

                    # Show tabs
                    tab1, tab2 = st.tabs(["📄 Tailored CV", "✉️ Cover Letter"])
                    with tab1:
                        st.markdown(cv_md)
                        # CV specific CSS (line-height 1.15, includes .date style)
                        cv_css = """
                        @page { size: A4; margin: 2cm; }
                        body {
                            font-family: 'Calibri', 'Arial', sans-serif;
                            font-size: 11pt;
                            line-height: 1.15;
                            margin: 0;
                        }
                        h1 { font-size: 18pt; font-weight: bold; margin-bottom: 0.5em; }
                        h2 { font-size: 14pt; font-weight: bold; border-bottom: 1px solid #ccc; margin-top: 1em; margin-bottom: 0.5em; }
                        p, li { margin-bottom: 0.3em; }
                        ul { padding-left: 1.5em; }
                        .date { float: right; font-weight: normal; color: #555; }
                        """
                        cv_html = markdown.markdown(cv_md, extensions=['extra'])
                        cv_pdf = HTML(string=f"<html><head><meta charset='UTF-8'><style>{cv_css}</style></head><body>{cv_html}</body></html>").write_pdf()
                        st.download_button("⬇️ Download CV as PDF", data=cv_pdf, file_name="tailored_cv.pdf", mime="application/pdf")
                    with tab2:
                        st.markdown(cover_md)
                        # Cover letter CSS (line-height 1.25, no .date needed)
                        cover_css = """
                        @page { size: A4; margin: 2cm; }
                        body {
                            font-family: 'Calibri', 'Arial', sans-serif;
                            font-size: 11pt;
                            line-height: 1.25;
                            margin: 0;
                        }
                        .sender-address {
                            margin-bottom: 2cm;
                            font-size: 9pt;
                            line-height: 1.2;
                        }
                        .recipient-address {
                            margin-bottom: 1cm;
                            font-size: 9pt;
                        }
                        .date {
                            text-align: right;
                            margin-bottom: 1cm;
                        }
                        .subject-line {
                            font-size: 14pt;
                            font-weight: bold;
                            margin: 1em 0 0.5em 0;
                        }
                        p {
                            margin-bottom: 0.5em;
                        }
                        h1 { font-size: 18pt; font-weight: bold; margin-bottom: 0.5em; }
                        h2 { font-size: 14pt; font-weight: bold; border-bottom: 1px solid #ccc; margin-top: 1em; margin-bottom: 0.5em; }
                        p, li { margin-bottom: 0.3em; }
                        """
                        cover_html = markdown.markdown(cover_md, extensions=['extra'])
                        cover_pdf = HTML(string=f"<html><head><meta charset='UTF-8'><style>{cover_css}</style></head><body>{cover_html}</body></html>").write_pdf()
                        st.download_button("⬇️ Download Cover Letter as PDF", data=cover_pdf, file_name="cover_letter.pdf", mime="application/pdf")

                except Exception as e:
                    st.error(f"Error: {str(e)}")
    elif generate and not jd_text:
        st.warning("Please paste a job description.")
    elif generate and not api_key:
        st.warning("Please provide your Gemini API key.")
    else:
        # Show previously generated documents (if any)
        if "cv_md" in st.session_state:
            tab1, tab2 = st.tabs(["📄 Tailored CV", "✉️ Cover Letter"])
            with tab1:
                st.markdown(st.session_state["cv_md"])
                cv_css = """
                body {
                    font-family: 'Calibri', 'Arial', sans-serif;
                    font-size: 11pt;
                    line-height: 1.15;
                    margin: 2cm;
                }
                h1 { font-size: 18pt; font-weight: bold; }
                h2 { font-size: 14pt; font-weight: bold; border-bottom: 1px solid #ccc; }
                .date { float: right; color: #555; }
                ul { padding-left: 1.5em; }
                """
                cv_html = markdown.markdown(st.session_state["cv_md"], extensions=['extra'])
                cv_pdf = HTML(string=f"<html><head><meta charset='UTF-8'><style>{cv_css}</style></head><body>{cv_html}</body></html>").write_pdf()
                st.download_button("⬇️ Download CV as PDF", data=cv_pdf, file_name="tailored_cv.pdf", mime="application/pdf")
            with tab2:
                st.markdown(st.session_state["cover_md"])
                cover_css = """
                @page { size: A4; margin: 2cm; }
                body {
                    font-family: 'Calibri', 'Arial', sans-serif;
                    font-size: 11pt;
                    line-height: 1.25;
                    margin: 0;
                }
                .sender-address {
                    margin-bottom: 2cm;
                    font-size: 9pt;
                    line-height: 1.2;
                }
                .recipient-address {
                    margin-bottom: 1cm;
                    font-size: 9pt;
                }
                .date {
                    text-align: right;
                    margin-bottom: 1cm;
                }
                .subject-line {
                    font-size: 14pt;
                    font-weight: bold;
                    margin: 1em 0 0.5em 0;
                }
                p {
                    margin-bottom: 0.5em;
                }
                h1 { font-size: 18pt; font-weight: bold; }
                h2 { font-size: 14pt; font-weight: bold; border-bottom: 1px solid #ccc; }
                """
                cover_html = markdown.markdown(st.session_state["cover_md"], extensions=['extra'])
                cover_pdf = HTML(string=f"<html><head><meta charset='UTF-8'><style>{cover_css}</style></head><body>{cover_html}</body></html>").write_pdf()
                st.download_button("⬇️ Download Cover Letter as PDF", data=cover_pdf, file_name="cover_letter.pdf", mime="application/pdf")

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 0.85rem;'>Made with ❤️ for job‑winning human career stories.</p>", unsafe_allow_html=True)