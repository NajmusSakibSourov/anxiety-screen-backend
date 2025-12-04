# AGENTS.md - AI Agent Instructions for AnxietyScreen

## 🎯 Project Overview

You're building **AnxietyScreen** for someone with **limited coding experience (Vibe-Coder)**. The user is committed to a **No-Code Only** approach for the UI and needs the AI to manage the necessary Python backend code. Please:
- Explain complex concepts simply (e.g., Serverless, API, Python dependencies)
- Provide working Python code for the Cloud Function with clear comments
- Balance simplicity with best practices for a low-data, $0 budget environment
- The main goal is a rapid deployment (**ASAP**) to meet the research paper deadline

## 📚 What We're Building

**App:** AnxietyScreen
**Purpose:** A free, private AI check-up for Bangladeshi students.
**Tech Stack (Hybrid No-Code):**
- **Frontend/UI:** **Softr or Webflow (Free Tier)**: A visual builder used for the static pages, responsive design, and form creation. This is the **No-Code** part.
- **Backend/Database:** **Airtable (Free Tier)**: Used as the simple, visual database for storing anonymous user data, survey submissions, and localized support content.
- **AI Processing:** **Google Cloud Functions (or AWS Lambda)**: A serverless environment to run the single, lightweight **Python script** with Scikit-learn to handle the ML prediction.
- **Deployment Platform:** **Vercel or Netlify (Free Tier)**: Used for fast, reliable hosting of the static UI and ensuring the **3-second load time** constraint is met.
**Learning Goals:** Understanding the data flow between a No-Code UI, a visual database, and an AI-managed serverless API endpoint.

## 🛠 Setup Instructions

### Prerequisites Check (AI will manage the Python environment)
```bash
# The user (Vibe-Coder) will focus on setting up accounts.
# The AI must be prepared to generate the Python code, requirements.txt, and deployment steps.

# Python requirements for the Cloud Function:
pandas
scikit-learn
flask # Or similar micro-framework for the Cloud Function entry point