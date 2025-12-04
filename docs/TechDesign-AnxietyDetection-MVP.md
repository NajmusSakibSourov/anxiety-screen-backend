Technical Design Document: AnxietyScreen MVP
🛠 How We'll Build It
Recommended Approach: Hybrid No-Code, Serverless Architecture

This approach is specifically chosen to meet your three non-negotiable requirements:

    No-Code Only (for you): You will use a visual builder for the entire user interface.

    $0 Budget: All recommended tools have generous free tiers.

    Python ML Required: The AI will create and manage a Python function for the ML model.

Component	Recommended Tool (The Best Solution)	Rationale for Your Constraints
Frontend/UI (The No-Code Part)	Softr or Webflow (Free Tier)	Easiest, Fastest UI Build. These platforms allow for quick, responsive, visual development that handles the "Calm, Low-Data" vibe without writing code.
Database/Auth	Airtable (Free Tier)	Simplest Database and Anonymous Registration. Excellent visual interface for managing survey data and storing anonymous user profiles. It is easy to connect to Softr/Webflow.
Backend/AI Processing	Google Cloud Functions or AWS Lambda (Free Tier)	Runs Python ML Code on Demand. The only way to run Python/Scikit-learn with a $0 budget. The AI will write the Python function for you.
Deployment/API Gateway	Vercel or Netlify (Free Tier)	Fastest Deployment and Performance. Perfect for hosting the static UI and ensuring the 3-second load time constraint is met.
Alternative Options Compared
Option	Pros	Cons (Why we avoid it)	Cost	Time to MVP
Full No-Code ML Platform	Zero code, easy	Most of these platforms cost money (e.g., Bubble/Adalo's paid plans) and often don't support custom Python ML models.	$50+/mo (Too expensive)	2-3 Weeks
Python Framework Only	High performance, perfect code control	Requires high code proficiency (Flask/Django) and a steep learning curve. Violates "No-Code" request.	$0 (if free hosting)	8+ Weeks
📋 Project Setup Checklist (ASAP Timeline)
Step 1: Create Accounts (Day 1)

    [ ] Softr/Webflow account (Visual UI Builder)

    [ ] Airtable account (Database)

    [ ] Google Cloud or AWS account (Serverless Function)

    [ ] Vercel or Netlify account (Hosting)

Step 2: AI Assistant Setup (Day 1)

    [ ] Install Cursor or Windsurf (Best for guiding code)

    [ ] Configure with API key

    [ ] Use AI to generate the Python ML Model Script.

🏗 Building Your Features: Implementation Plan

The entire application flow is a sequential process: Collect Data → Process Data → Show Results.
Feature 1: Anonymous User Registration (The Airtable & Softr/Webflow Part)

Complexity: ⭐☆☆☆☆ (Easy)

How to build with No-Code:

    Database Setup (Airtable):

        Create a base named AnxietyScreen_DB.

        Create a table named Users with fields: Anon_ID (auto-generated), Age, Location, Test_Count.

    UI Setup (Softr/Webflow):

        Use a basic Form Block.

        Connect the form to the Users table in Airtable.

        The form stores the anonymous data, and the platform handles the session.

Feature 2: AI-Driven GAD-7 Survey Module (The Airtable & Serverless Part)

Complexity: ⭐⭐⭐☆☆ (Medium - AI-Managed Code)

How to build with AI-Managed Code:

    Data Structure (Airtable):

        Create a table named Survey_Submissions.

        Fields: User_ID, Q1_Score, Q2_Score... through Q7_Score.

        Crucial Field: Response_Time (The UI needs a simple script to measure the time from page load to form submission).

    The Trigger (AI Prompt for Code):

        Ask your AI assistant (e.g., Cursor): "Write a Python script for Google Cloud Functions/AWS Lambda that receives 8 inputs (7 GAD scores + 1 response time), loads a pre-trained Scikit-learn Logistic Regression model, runs the prediction, and returns 'Low,' 'Moderate,' or 'High' anxiety. The script must be under 128MB for the free tier."

    The API Connection (Softr/Webflow):

        The No-Code form is configured to send the data directly to the URL of the newly created Python Serverless Function.

Feature 3: Immediate ML Prediction & Classification

Complexity: ⭐☆☆☆☆ (Easy - API consumption)

This is handled by the result of the function in Feature 2.
Feature 4: Personalized, Localized Feedback Dashboard

Complexity: ⭐⭐☆☆☆ (Easy-Medium)

How to build with No-Code:

    Logic: Use the No-Code platform's native logic functions (e.g., Softr's Conditional Display).

    Display: The dashboard is built with three main sections, all written in Bengali (as required):

        IF Prediction = "Low Anxiety": SHOW Motivational text block.

        IF Prediction = "Moderate Anxiety": SHOW Self-Help Tips text block.

        IF Prediction = "High Anxiety": SHOW Emergency Hotline text block.

    Performance Check: Since the UI is mostly static text (not dynamic charts or complex animations), the load time will be minimal, meeting the 3-second constraint.

🎨 Design Implementation
Matching Your PRD Vibe: "Calm, Private, Low-Data, Bengali-First"

    UI Tool: Webflow or Softr are ideal because they generate clean, lightweight HTML/CSS that loads quickly.

    Aesthetic: Use a Soft Color Palette (light blues, pastel greens, off-white backgrounds). Avoid dark mode and heavy images.

    Font: Use an accessible, low-weight Bengali font (e.g., Siyam Rupali or Lohit Bengali) to ensure clear readability.

📊 Database & Data Storage
Database Setup: Airtable (Free Tier)
Table	Purpose	Key Fields
Users	Anonymous registration, session tracking	Anon_ID (PK), Age, Location, Last_Test_Date
Survey_Submissions	Stores raw GAD-7 and behavioral data	User_ID (FK), Q1-Q7 Scores, Response_Time (Crucial), Final_Prediction
Support_Content	Stores localized feedback messages	Category (Low/Mod/High), Bengali_Message, Hotline_Number
🤖 AI Assistance Strategy (Your Safety Net)

Your biggest worries are getting stuck and making the wrong choices. Your AI assistant will act as your Technical Co-Pilot and Debugger.
Task	Best AI Tool Strategy	Rationale for Vibe-Coder
Core ML Python Script	Cursor/Windsurf (Code Generation)	Generates the entire Python function code for you. You don't write it, you just deploy it.
Debugging Errors	ChatGPT/Claude (Explanation)	If a function breaks, copy the error message and ask: "Explain this error in simple terms and tell me exactly where to paste the fix."
Making Tech Choices	Claude Sonnet 4.5 (Architecture Reasoning)	Use this document as your guide, but if you need to choose between two tools, ask Claude for a cost/performance trade-off analysis.
Simple Code Snippets	GitHub Copilot/Cline	For quick needs like the Response_Time Javascript code snippet, use Copilot for fast suggestions inside your editor.
🚀 Deployment Plan (ASAP Focus)
Recommended Platform: Vercel (Free Tier)

Vercel is the fastest way to deploy modern web applications and is critical for hitting your ASAP timeline and 3-second load time.
Deployment Steps:

    UI Deploy: Connect your Softr/Webflow site to your custom domain or deploy the exported static files to Vercel via a simple drag-and-drop or Git connection.

    ML Deploy (AI-Assisted): Use the AI-generated Python code and deploy it to Google Cloud Functions (or AWS Lambda). This creates a simple API URL.

    Final Connection: Update the Softr/Webflow form to submit data to the API URL from the Serverless Function.

💰 Cost Breakdown
Service	Free Tier	Cost at MVP Scale
Hosting (Vercel/Netlify)	Generous bandwidth	$0
Database (Airtable)	1,000 records/base, 50 automations	$0
AI Backend (Google Cloud Functions)	2 million free calls/month	$0
UI Builder (Softr/Webflow)	Limited pages/storage	$0
AI Assistant (Cursor/Windsurf)	Paid subscription recommended	$20/month (The only suggested cost, but it's optional)
Total Monthly Cost		$0 - $20

I've created your complete Technical Design Document above. This document defines HOW you will build your app using a low-risk, high-performance, and free-tier architecture, even with the Python ML requirement.

Next Steps:

    Review the TDD - Specifically the recommended tools and the breakdown of the 4 core features.

    Start Setting Up - Create accounts for Softr/Webflow and Airtable to begin building the UI.

    Proceed to Part IV to create your User Stories and Epics.