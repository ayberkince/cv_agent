# Project CV Summary: Mayzyyy Schedule

A professional summary, technical breakdown, and ready-to-use resume bullet points for the **Mayzyyy Schedule** (Mayzyyy Command) project.

---

## 📋 Short Project Description (For CV Project Section)
**Mayzyyy Schedule** is an offline-first desktop task management and cognitive assistance application specifically designed for individuals with ADHD or executive dysfunction. It combines interactive scheduling, cognitive energy-based task filtering, gamified rewards, and integrated LLM capabilities to reduce decision paralysis and optimize productivity. Built as a cross-platform desktop application using Rust (Tauri v2) and React/TypeScript.

---

## 🛠️ Core Tech Stack & Libraries
* **Desktop Runtime Environment**: Rust (via Tauri v2 desktop framework)
* **Frontend Framework & Language**: React 19, TypeScript, Vite
* **State Management & Persistence**: LocalStorage API for offline-first resilience
* **UI/UX & Animations**: Framer Motion (fluid, high-performance UI transitions), Lucide React (vector icon systems)
* **AI Integration**: Google Generative AI SDK (using the Gemini API)
* **Calendar Engine**: FullCalendar (`dayGrid`, `timeGrid`, `multiMonth`, and `interaction` plugins)
* **Interactive Media & Gamification**: Web Audio API (dynamic real-time sound synthesis), Canvas Confetti (particle physics animations)

---

## 🌟 Key Technical Features Implemented
1. **Cognitive Energy-Based Filters & Survival Mode**:
   * Designed a tri-tier energy architecture (`spicy`, `fidget`, `dopamine`) to classify tasks by mental load.
   * Created dynamic UI "ghosting" to fade out heavy tasks during low-focus states.
   * Developed a minimalist **"Survival Mode"** that strips away scheduling complexity to display only fundamental daily bio-routines (hydration, medication, walks) alongside a single focus task.
2. **Conversational AI Command Center**:
   * Integrated Gemini LLMs to parse natural-language user "brain dumps" into structured JSON payloads.
   * Dynamically mutates application state to add, complete, or delete schedule items based on AI intent resolution.
3. **Task Fracturing & Meeting Buffer Management**:
   * Built an AI-driven task-deconstruction engine that breaks complex/intimidating items into simple, low-friction physical micro-steps to overcome executive dysfunction paralysis.
   * Programmed an automated meeting buffer manager that detects terms like "meeting" or "call" and preemptively schedules 15-minute Prep and Decompress buffers around the block.
4. **Professional Hype File Ledger & Corporate speak Translator**:
   * Implemented a professional translation feature that utilizes LLMs to turn raw, blunt, or emotional inputs into polished corporate communications.
   * Built a "Hype File" system that archives shredded high-stress tasks, generating structured bullet points suitable for professional performance reviews.
5. **Interactive Audio-Visual System**:
   * Developed a synthesized sound library using the native **Web Audio API** to generate organic sound effects (`clack`, `shred`, `zen`, `anchor`) programmatically without loading external asset files.
   * Added micro-animations, confetti, and screen shakes to build a positive feedback loop for task completion.

---

## ✍️ Ready-to-Use CV Bullet Points (Action-Oriented)

* **Architected and developed a cross-platform desktop task management application** using **Rust (Tauri v2)** and **React / TypeScript**, optimizing accessibility for users facing executive dysfunction.
* **Integrated Gemini LLMs via the Google Generative AI SDK** to enable conversational natural-language scheduling, task parsing, and context-aware task fracturing to reduce cognitive load.
* **Engineered a dynamic energy-state UI system** featuring Hype File archiving, meeting buffer insertion, and a distraction-free "Zen Mode" utilizing **Framer Motion** and the **Web Audio API** for interactive feedback.
* **Implemented an offline-first architecture** with resilient browser storage, multi-view calendar layouts (**FullCalendar**), and real-time state persistence.
