# Project Summary: AI News Intelligence Dashboard

This document provides a professional summary of the **AI News Intelligence** project, structured for use in a Curriculum Vitae (CV), resume, or portfolio.

---

## 📋 Elevator Pitch / Summary
Developed a full-stack market monitoring and business intelligence application that harvests real-time global news headlines, structures data via an automated ETL pipeline, and stores it in a relational database. Built a custom Retrieval-Augmented Generation (RAG) assistant and vector semantic search engine using Google Gemini embedding/text models to synthesize trends, identify narrative drift ("Delta Engine"), and answer natural language inquiries from stored market intelligence.

---

## ⚡ Core Technical Highlights

* **Automated Data Ingestion (ETL):** Designed and implemented an automated ETL pipeline that extracts raw US news headlines from NewsAPI, executes custom sanitization workflows to filter duplicate stories, and loads them dynamically into a SQLite database.
* **Vector Embeddings & Semantic Search:** Built a custom vector retrieval system using `numpy` cosine similarity and direct REST API integrations with Google's `gemini-embedding-001` model, bypassing SDK deprecation issues to store and index semantic document memories.
* **Retrieval-Augmented Generation (RAG):** Engineered a senior-analyst LLM agent (`gemini-2.5-flash`) that answers complex queries based *exclusively* on context retrieved from historical database headlines, implementing strict hallucination safeguards.
* **Narrative Shift Analytics ("Delta Engine"):** Programmed comparison algorithms to calculate narrative drift across historical reports, automatically classifying emerging, persistent, and fading topics between any two point-in-time database snapshots.
* **Data Visualization & Dashboarding:** Created a responsive, premium web dashboard using **Streamlit** (injected with custom CSS/styling) featuring metric components, topic frequency trends over rolling timeframes, and interactive charts.
* **Resilient API Integration:** Structured robust safety guardrails and quota-handling logic to prevent API blocks during high-volume synthesis of potentially sensitive headlines.

---

## 🛠️ Technology Stack

| Category | Technologies |
| :--- | :--- |
| **Frontend & UI** | Streamlit, HTML5, Custom CSS Injection |
| **Artificial Intelligence** | Google Gemini API (`gemini-2.5-flash`, `gemini-embedding-001`), RAG, Custom Semantic Embeddings Vector Engine |
| **Data Engineering** | Python, SQLite3, Pandas, NumPy, Collections, Requests, REST APIs |
| **Logging & Config** | Python Logging, Dotenv (`python-dotenv`), Pip / Requirements |
