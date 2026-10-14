# BrandShield — Digital Brand Risk Protection

## Overview
BrandShield is a hackathon prototype designed to help identify and monitor suspicious social media profiles and mobile applications that may impersonate legitimate brands.

The platform provides a dashboard for reviewing potential brand risks, viewing detection records, and exploring demo scan results.

## Problem Statement
Brand impersonation can mislead customers, damage trust, and expose people to scams. Finding suspicious profiles and applications can be difficult without a centralized monitoring interface.

## Solution
BrandShield provides a centralized dashboard to:
- View potential brand impersonation risks.
- Review detection records and risk indicators.
- Run a demonstration scan using sample data.
- Manage brand profiles.
- Access monitoring and health-check endpoints.

## Key Features
- Dashboard for brand-risk monitoring.
- Detection records and risk status indicators.
- Demo scanning workflow.
- Brand profile management.
- Django-powered backend.
- Responsive interface with static assets served through WhiteNoise.

## Technology Stack
- Python
- Django
- HTML, CSS and JavaScript
- SQLite for local development
- WhiteNoise for static files

## Run Locally

1. Clone the repository:

   `git clone https://github.com/AnuhyaSirasanagondla/BrandShield.git`

2. Open the project directory:

   `cd BrandShield`

3. Create and activate a virtual environment:

   **Windows PowerShell**
   
   `python -m venv .venv`

   `.\.venv\Scripts\Activate.ps1`

4. Install dependencies:

   `pip install -r requirements.txt`

5. Apply database migrations:

   `python manage.py migrate`

6. Collect static files:

   `python manage.py collectstatic --noinput`

7. Start the development server:

   `python manage.py runserver`

8. Open `http://127.0.0.1:8000/` in your browser.

## Important Note
This is a hackathon prototype. Demo scan results use illustrative sample data and do not represent verified live monitoring of social media platforms or mobile app stores.

## Future Enhancements
- Integrate authorized social media and app-store data sources.
- Add explainable AI-based risk scoring.
- Enable alerts for newly detected impersonation attempts.
- Improve reporting and trusted-contact workflows.

## Team
Developed for HacXLerate 2026.

## License
For hackathon demonstration and educational purposes.
