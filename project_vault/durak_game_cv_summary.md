# Durak Elite: Real-Time Multiplayer Tactical Card Game

Below is a structured description of the **Durak Elite** project, written in a professional tone suitable for a CV/resume. It contains a high-level summary, key bullet points detailing your technical achievements, and a breakdown of the technology stack.

---

### Project Summary
**Durak Elite** is a real-time, multiplayer implementation of the popular strategic card game Durak, built around a high-fidelity espionage and security dossier theme. The application features a custom-built object-oriented game engine, low-latency bidirectional socket communication, client-side predictive AI recommendations, and an integrated profile economy tracked via cloud databases.

---

### CV Bullet Points (Impact-Focused)

* **Real-Time Multiplayer Architecture:** Engineered a decoupled full-stack architecture using **Next.js (App Router, TypeScript)** and a dedicated **Express / Node.js** backend synchronized in real time via **Socket.io** with < 80ms latency tracking.
* **Custom Object-Oriented Game Engine:** Built a state-driven game engine in **TypeScript** to model complex rules (Attack, Defend, Transfer/Perevodnoy), manage game flows (e.g., lowest-trump starting calculations), and handle dynamic 2-to-6 player matchmaking lobbies.
* **Security & "Fog of War" Protocol:** Architected a secure state-broadcasting model on the backend that strips opponent card values and replaces them with `{ hidden: true }` metadata prior to network dispatch, eliminating client-side memory inspection and cheating.
* **Client-Side Predictive AI ("Consultant Mode"):** Developed a local rule-based AI advisor that analyzes table cards, card values, and trump suits to recommend the mathematically optimal card to play, defend with, or action to take.
* **Intelligent Responsive Layouts:** Programmed a mathematical seating algorithm using trigonometric formulas (`Math.sin`/`Math.cos`) to dynamically distribute opponent card fans along a semi-circular virtual felt table across mobile and desktop viewports.
* **Database & Dynamic Game Economy:** Integrated **MongoDB (via Mongoose)** to orchestrate user accounts, persist career stats (Wins/Losses/Total Played), and implement a stakes-based virtual lobby currency model.
* **High-Fidelity UI/UX:** Styled a premium, cohesive "secret agent" dashboard featuring custom animations (**Framer Motion**), micro-interactions (card hover fans, shake effects on invalid plays), and an active client emoji/reaction broadcast system.

---

### Technology Stack & Tools Used

| Layer | Technologies & Frameworks |
| :--- | :--- |
| **Frontend** | React 19, Next.js 15 (App Router), TypeScript, Tailwind CSS, Framer Motion |
| **Backend** | Node.js, Express, Socket.io, TypeScript, Nodemon |
| **Database & Caching** | MongoDB Atlas, Mongoose, Redis / ioredis (scaling architecture ready) |
| **Deployment & Tooling** | Git, npm, PostCSS, ESLint |

---

> [!TIP]
> **Suggested Resume Heading:**
> **Durak Elite — Full-Stack Real-Time Multiplayer Web Application** *(Next.js, TypeScript, Node.js, Socket.io, MongoDB)*
