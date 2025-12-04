Product Requirements Document: AnxietyScreen MVP
🎯 Product Overview

App Name: AnxietyScreen Tagline: A free, private AI check-up for Bangladeshi students. Launch Goal: Publish a research paper (validate the AI model's effectiveness). Target Launch: 8 Weeks (Allows for focused development and data validation).
👥 Who It's For
Primary User: Riya

Riya is a 16-year-old high school student in a rural area of Bangladesh. She is focused on her studies but faces intense academic and familial pressure. She primarily accesses the internet via a shared mobile phone or older smartphone on an unstable 3G connection.

Their Current Pain:

    Intense stress and anxiety with nowhere safe to turn.

High social stigma surrounding mental health prevents her from asking for help.

Existing mental health apps are too costly, use too much data, or are not in Bengali.

What They Need:

    A safe, anonymous way to check her emotional state.

An instant, localized suggestion she can act on immediately.

    An app that loads instantly and doesn't cost her money or data.

Example User Story

"Meet Riya, a high school student who struggles with overwhelming exam pressure and the shame of feeling anxious. Every day she fears judgment if she speaks up. She needs a private, low-data app that quickly tells her if she needs help and what she can do right now, so she can get back to her studies with a clearer mind."
🔧 The Problem We're Solving

The core problem is the limited access to mental health support and awareness among high school students in rural Bangladesh. This project bridges that gap by providing a simple, accessible, and AI-driven web solution that can quickly assess anxiety levels.

Why Existing Solutions Fall Short:

    Local Professional Apps (Relaxy): They are based around paid counseling services and often rely on heavier, data-intensive mobile apps.

Global Self-Help Apps (Calm): They are primarily in English, require better internet, and are not culturally or linguistically localized.

Academic Forms (Paper GAD-7): They provide a score but offer no immediate, personalized feedback or behavioral analysis.

🎬 User Journey
Discovery → First Use → Success

    Discovery Phase

        How they find us: A community message board or school announcement link.

        What catches their attention: The tagline "Free, Private Stress Check-up" in Bengali.

        Decision trigger: The need for validation and a lack of data usage fear.

    Onboarding (First 5 Minutes)

        Land on: The minimalist landing page.

        First action: Basic, anonymous registration.

        Quick win: Starting the quick GAD-7 based survey.

Core Usage Loop

    Action: Riya completes the survey, and the system tracks her response times and interaction behavior.

Reward: The AI model classifies her anxiety as Low, Moderate, or High.

Investment: The app provides personalized, localized self-help tips based on her result.

Success Moment

    "Aha!" moment: When she sees the immediate result and receives a concrete, understandable Bengali self-help tip, she feels validated and empowered.

        Share trigger: She recommends the app to a friend who is also struggling with exam stress.

✨ MVP Features
🔴 Must Have for Launch (P0)
1. Anonymous User Registration

    What: Allows students to create an account using minimal, non-identifying information (e.g., age, location) while guaranteeing anonymity and data encryption.

User Story: As a private student, I want to sign up without sharing my name so that I can use the app without social fear.

Success Criteria:

    [x] Basic fields (age/location) are stored securely.

[x] The system can retrieve a user's previous test history.

    Priority: P0 (Critical)

2. AI-Driven GAD-7 Survey Module

    What: A minimal, low-data UI that displays the GAD-7 questions and records user responses on a 0-3 scale. The system must track response times and interaction behaviors in the background.

User Story: As an anxious student, I want a simple set of clear questions so that I can easily complete the assessment quickly on my mobile phone.

Success Criteria:

    [x] All 7 questions are stored in the DB upon completion.

[x] Response time for each question is logged.

    Priority: P0 (Critical)

3. Immediate ML Prediction & Classification

    What: The backend ML model (Logistic Regression or Random Forest) processes the combined GAD-7 score and behavioral data to classify anxiety into Low, Moderate, or High.

User Story: As a researcher, I want the AI model to quickly classify the anxiety level so that I can validate the core research hypothesis.

Success Criteria:

    [x] Classification result is returned in < 500ms.

    [x] Prediction is displayed on the dashboard.

    Priority: P0 (Critical)

4. Personalized, Localized Feedback Dashboard

    What: A dashboard that immediately displays the classification result (Low/Moderate/High) and provides customized, Bengali-first advice (e.g., deep breathing tips for Moderate, emergency advice for High).

User Story: As an anxious student, I want to see immediate, practical suggestions so that I can manage my feelings right now.

Success Criteria:

    [x] Appropriate feedback message is displayed for each classification level.

[x] High anxiety users are shown emergency advice/hotlines.

    Priority: P0 (Critical)

🚫 NOT in MVP (Saving for Later)

    Admin Panel: Will add after the research paper is validated. Building this is time-consuming and unnecessary for the primary user flow.

Chatbot or Voice Support: Deferred because it adds significant technical complexity (NLP/APIs) and heavy data usage, violating the low-bandwidth constraint.

Counselor/Teacher Referral System: Too complex for MVP, involving external integration and high regulatory risk. The current advice (FDB-4.2) is sufficient.

Why we're waiting: Keeps MVP focused on the research goal and launchable in 8 weeks.
📊 How We'll Know It's Working
Launch Success Metrics (First 30 Days)
Metric	Target	Measure
Survey Completion Rate	> 85%	Track users who start the GAD-7 survey vs. those who complete it.
Low-Bandwidth Prediction Success Rate	> 95%	Track sessions where the survey submission to result display process succeeds under 3G simulation.
Growth Metrics (Months 2-3)
Metric	Target	Measure
Returning User Rate	> 30%	Track users who complete a second survey within 30 days (Proves retention and perceived value).
🎨 Look & Feel

Design Vibe: Calm, Private, Low-Data, Bengali-First

Visual Principles:

    Minimalist & Clear: Simple UI with minimal text and no unnecessary graphics.

Soft Tones: Use a calming color palette (e.g., soft blues, greens).

Mobile First: Responsive design to work flawlessly on low-end mobile devices.

Key Screens/Pages:

    Registration/Login: Simple, single-page form.

    Survey Module: Single question displayed at a time for focus and data logging.

    Results Dashboard: Prominently displays classification and tailored advice.

Simple Wireframe

[Mobile Screen/Survey Page]
┌─────────────────────────┐
│     [Header/Logo]       │
├─────────────────────────┤
│                         │
│      [Question 3/7]     │
│                         │
├─────────────────────────┤
│     [Option A (0)]      │
│     [Option B (1)]      │
│     [Option C (2)]      │
│     [Option D (3)]      │
├─────────────────────────┤
│       [Next Button]      │
└─────────────────────────┘

⚡ Technical Considerations

Platform: Web Application Responsive: Yes, mobile-first Performance: Page load < 3 seconds on 3G ML Model: Logistic Regression (Baseline) or Random Forest Backend: Python (Flask or Django) Database: PostgreSQL or Firebase / Supabase (Free-tier friendly) Security: HTTPS, Data encrypted and anonymized

💰 Budget & Constraints

Development Budget: Minimal (Team time only)

Monthly Operating: $0 (Must use free-tier tools) Timeline: 8 Weeks to launch Team: IUB Team (2 students)

🚀 Launch Strategy (Brief)

Soft Launch: Limited private beta with a select group of high schools in rural areas to gather initial data for the paper. Target Users: 50-100 beta users. Feedback Plan: Direct testing and bug reporting to the IUB development team via a simple contact form.

Iteration Cycle: Rapid fix cycle based on supervisor and QA feedback.

✅ Definition of Done for MVP

The MVP is ready to launch when:

    [x] All P0 features (1-4) are functional.

    [x] The system successfully classifies anxiety (MLD-3.1/3.2).

[x] Low-bandwidth performance goal is met (3-second load).

[x] Anonymization and encryption are confirmed.

[x] The full user journey works end-to-end.

[x] Final verification via live demo of the working prototype is completed.

📝 Next Steps

After this PRD is approved:

    Create Technical Design Document (Part III)

    Set up the development environment (Python/React/Firebase)

    Build MVP with AI assistance

    Test with 5-10 beta users

    Launch! 🎉