# Project Summary: Begleit – Trusted Non-Medical Support Marketplace

A robust, secure two-sided marketplace connecting clients requiring non-medical support (e.g., medical appointment accompaniment, light paperwork assistance, and companionship) with verified, local helpers.

## Technical Stack
*   **Frontend & Core Framework:** Next.js (App Router), React 19, TypeScript
*   **Styling & UI:** Tailwind CSS, PostCSS, Radix UI Primitives, Motion (Framer Motion), Lucide React
*   **Database & ORM:** PostgreSQL, Prisma ORM
*   **Authentication & Security:** NextAuth.js, Clerk Auth
*   **API & AI Integration:** Google Gemini API (`@google/genai` SDK)

---

## Key Features & Contributions (Resume-Ready Bullet Points)

*   **Architected a Two-Sided Marketplace System:** Built a responsive, mobile-first marketplace web application utilizing Next.js App Router and Prisma to connect clients and non-medical assistants.
*   **Engineered a Transaction & Financial Booking Engine:** Designed a robust state-machine for booking life-cycles (`PENDING`, `CONFIRMED`, `IN_PROGRESS`, `COMPLETED`, `CANCELED`) with an automated financial ledger system calculating helper earnings, platform fees, and tracking simulated payment/payout states.
*   **Implemented Trust & Safety Infrastructure:** Developed user moderation tools, safety report filing, enforcement level systems (`WARNING`, `RESTRICTED`, `SUSPENDED`, `BANNED`), and manual helper verification workflows to guarantee platform safety.
*   **Built Real-Time Communication Channels:** Implemented a booking-specific in-app messaging/chat system enabling clients and helpers to safely coordinate logistics.
*   **Designed Operator / Admin Control Panels:** Created a comprehensive administrator dashboard allowing operators to manage users, review support reports, verify helper credentials, and handle disputes/refunds.
*   **Integrated Modern Authentication:** Configured secure, role-based authentication using Clerk and NextAuth.js to handle client, helper, and admin access control.
