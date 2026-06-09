# Project Summary: Retro OS Desktop Portfolio

A high-performance, interactive portfolio website featuring a vintage 90s Operating System (OS) desktop GUI. This project allows users to navigate projects, case studies, and bio details through a playful, retro-themed workspace with draggable windows, customizable physics, and an interactive trash bin collision system.

---

## 🛠️ Technology Stack & Tools Used

### Core Framework & Language
* **Next.js 15.4 (App Router)**: Utilizing React 19's server components, optimized routing, and server-side rendering characteristics to boot a highly interactive single-page desktop environment.
* **TypeScript (5.9)**: Implemented throughout for rigid type safety, robust state interfaces, and self-documenting code.
* **React 19**: Leveraged for hooks, state management, and modern component lifecycle execution.

### Styling & Animation
* **Tailwind CSS v4 (with PostCSS)**: Custom-configured utility utility classes utilizing custom CSS custom properties (variables) to maintain a cohesive high-contrast editorial pixel theme (colors: `brand-blue`, `brand-cream`, etc.).
* **Motion (formerly Framer Motion v12)**: Powering fluid spring physics, drag gestures, desktop collision boundaries, and bounciness. Controls the draggable desktop windows and animated modal transitions.
* **Lucide React & Custom SVGs**: Used for retro vector icons, pixel hearts, and vintage directory folders.

### State & Interaction Hooks
* **Custom Window Manager (`useWindowManager`)**: Manages dynamic z-indexing and window focus state, bringing active windows to the front when clicked or dragged.
* **Custom Trash System (`useTrashSystem` & collision detection)**: Implements physical collision detection. Dragging a project window (`.exe`) over the Trash icon automatically deletes it, prompting updates to desktop folders and enabling item restoration.
* **Custom Responsive Hooks (`useIsMobile`)**: Dynamically samples screen viewports to ensure seamless layouts and responsiveness on desktop, tablet, and mobile screens.

### Development & Build Tooling
* **ESLint (v9) & eslint-config-next**: Strict code style linting and verification.
* **Firebase Tools (v15)**: Integrated for instant deployment, staging, and static hosting setups.

---

## 📝 CV / Resume Descriptions

Here are three tailored descriptions you can copy directly into your CV, depending on the format you use.

### Option 1: Bulleted Format (Standard Technical Resume)
> **Frontend Developer — Retro OS Desktop Portfolio** (Next.js, TypeScript, Tailwind CSS, Motion)
> * Developed a highly interactive 90s-inspired desktop operating system portfolio featuring physics-based window dragging, dynamic z-indexing, and interactive modals.
> * Implemented custom React hooks for global window management (`useWindowManager`) and dynamic responsive rendering on diverse viewport sizes.
> * Engineered an interactive trash system leveraging bounding-box collision detection in Framer Motion, enabling users to "drag and drop to delete" or restore items dynamically.
> * Structured styling guidelines using Tailwind CSS v4 and PostCSS, creating a cohesive, retro-modern aesthetic utilizing customized color tokens.

### Option 2: Short Paragraph Format (Chronological Resume)
> **Retro OS Desktop Portfolio | Next.js, TypeScript, Framer Motion, Tailwind CSS**
> Designed and built an interactive retro operating system desktop application that functions as a creative portfolio. Developed custom hooks to manage fluid drag physics, dynamic window z-indexing, and responsive designs across mobile and desktop. Integrated a collision detection trash system that allows users to drag window elements into the trash folder or restore deleted assets to the desktop. Used Next.js 15, TypeScript, Tailwind CSS v4, and Motion to build a fast, pixel-perfect, and highly engaging user experience.

### Option 3: Impact-focused Bulleted Format
> **Lead Developer & Designer — Interactive OS Portfolio**
> * **Creative Engineering**: Built a responsive, nostalgic 90s-style desktop portfolio featuring multi-window drag-and-drop mechanics using React 19 and Framer Motion.
> * **Dynamic Physics & UI**: Built custom hooks for layout coordinate tracking, dynamic z-index layers, and drag-and-drop collision systems to trash/restore files.
> * **Optimized Styling**: Maintained a design system with Tailwind CSS v4, keeping the site optimized, responsive, and lightweight.
