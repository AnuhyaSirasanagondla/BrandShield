# BrandShield — Digital Risk Protection

A hackathon prototype for the KAMPUS.VC Digital Risk Protection challenge. BrandShield helps a brand team review possible social-media impersonation and suspicious app listings with visible signals, a heuristic score, a recommended next step, a brand allowlist profile, and CSV export.

> **Prototype limitation:** the included detection examples are illustrative demo records. The scan endpoint stores sample detections in the Django database; it does not query Instagram, X, Google Play, Apple App Store, or any live source. Scores are triage signals, not proof that an account or app is malicious. Confirm evidence before reporting.

## Features
- Responsive BrandShield dashboard and monitoring views.
- Search/filter sample social profiles and app listings.
- Explainable detections: risk level, signal score, reason, and recommended manual review.
- Brand profile API that stores brand name, website, official handles, and publisher reference.
- Demo scan API that persists clearly labelled sample detections.
- Django admin for reviewing detections and brand profiles.
- CSV export from the dashboard.
- Health endpoint at `/api/health/`.

## Stack
- Python 3.11+ / Django 5.x
- SQLite for the hackathon prototype
- HTML, CSS, vanilla JavaScript
- Gunicorn + WhiteNoise for deployment

## Run locally

```bash
python -m venv .venv
# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. Check `http://127.0.0.1:8000/api/health/` for the API status. The first time you click **Run scan**, the demo scan endpoint stores three sample detections in SQLite. For the admin panel, run `python manage.py createsuperuser` and visit `/admin/`.

## Deploy on Render (today-friendly path)
1. Create a **public** GitHub repository and upload all files in this project folder.
2. In Render, create **New + → Web Service** and connect that repository.
3. Use these settings:
   - Runtime: Python
   - Build command: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - Start command: `gunicorn config.wsgi:application`
4. Add environment variables:
   - `SECRET_KEY`: a long random secret
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: your Render hostname, e.g. `brandshield-demo.onrender.com` (no protocol)
5. Deploy and open the public URL. Verify `/`, `/api/health/`, the scan button, profile save, and CSV export.

**Persistence warning:** Render's local filesystem may be ephemeral and SQLite is suitable only for a prototype. For reliable persistence after redeploys, attach a persistent disk or configure PostgreSQL before presenting this as a production service. Do not use the development SECRET_KEY in a public production environment.

## API quick test

Health:
```bash
curl https://YOUR-APP.onrender.com/api/health/
```

Run demo scan:
```bash
curl -X POST https://YOUR-APP.onrender.com/api/scan/ -H "Content-Type: application/json" -d '{}'
```

Save brand profile:
```bash
curl -X POST https://YOUR-APP.onrender.com/api/brand-profile/ -H "Content-Type: application/json" -d '{"brand_name":"Example Brand","website":"https://example.com","official_handles":"@example","official_publisher":"Example Inc"}'
```

## Challenge rubric mapping
- **Social media monitoring (30%)**: sample profile detection cards, search/filter, look-alike and added-word signals.
- **App store monitoring (30%)**: sample app records, publisher mismatch signals, search/filter.
- **Brand profile (15%)**: profile form and database-backed API; trusted handle/publisher references.
- **User experience (15%)**: uncluttered responsive dashboard, readable evidence and recommended next steps.
- **Presentation/demo (10%)**: run a scan, open a detection, explain its signals, show the official-asset safeguard, save profile, export CSV.
- **Bonus**: name variations are represented in the sample signals. A robust fuzzy-matching engine and live-source ingestion are future work and must not be claimed as completed.

## Suggested 3–5 person split
1. Frontend & responsive QA: dashboard layout, navigation, mobile browser testing.
2. Django/API: models, scan/profile endpoints, admin and database.
3. Detection logic: name normalization, similarity thresholds, allowlist and false-positive tests.
4. Deployment & GitHub: Render setup, README, environment variables, issue tracking.
5. Demo lead/QA: prepare test cases, verify links, capture screenshots and present limitations honestly.

## Demo script (2 minutes)
1. Start at Overview and explain the challenge: fake brand profiles and apps damage trust.
2. Click **Run scan**; explain that this prototype demonstrates the workflow with sample data, not live crawling.
3. Open a high-risk profile and explain each signal and the recommended manual verification step.
4. Open App Store Monitoring and show the publisher mismatch example.
5. Open Brand Profile, update the official handles/publisher and save.
6. Export the CSV report. Close by explaining how authorized APIs and PostgreSQL would support the next iteration.

## Before submission
- [ ] Public GitHub repository opens without login.
- [ ] Deployed public URL works on a second device/browser.
- [ ] `/api/health/` returns `{"status":"ok",...}`.
- [ ] Scan, profile save, detail modal, filters and CSV export work.
- [ ] README and screenshots are included.
- [ ] Team members have meaningful commits/issues/PRs.
- [ ] Demo records are described as sample data; no unsupported live-monitoring claims.
