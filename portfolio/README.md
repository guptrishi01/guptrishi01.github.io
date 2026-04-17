# Rishi Gupta — Portfolio

My personal portfolio site, built with Django. Showcases research, coursework, and personal projects in bioinformatics, machine learning, and full-stack development.

**Live site:** _(add URL after Render deploy)_

---

## Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── render.yaml              # Render deployment config
├── build.sh                 # Build script for Render
├── Procfile                 # Alternate host config
├── portfolio/               # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                    # Main app
│   ├── views.py
│   ├── urls.py
│   ├── projects_data.py     # ← Project content lives here (Python dict)
│   └── certifications_data.py
├── templates/
│   ├── base.html
│   └── core/
│       ├── home.html
│       ├── projects_index.html
│       ├── project_detail.html
│       └── certifications.html
└── static/
    ├── css/styles.css
    └── img/                 # Drop project hero images + headshot here
```

## Content model

No database is used for portfolio content. All project and certification content lives in two Python files:

- **`core/projects_data.py`** — one dict per project with methodology steps, code snippet, results, skills, etc.
- **`core/certifications_data.py`** — one dict per certification.

To add a project: append a dict to the `PROJECTS` list. To edit a project: edit the dict. Push to GitHub, redeploy on Render. Done.

## Local development

```bash
# Clone
git clone https://github.com/guptrishi01/portfolio.git
cd portfolio

# Virtual environment
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run dev server
python manage.py migrate
python manage.py runserver
# → http://127.0.0.1:8000/
```

## Deployment (Render)

1. Push this repo to GitHub (`github.com/guptrishi01/portfolio`).
2. On [Render](https://render.com), click **New → Blueprint**, point it at the repo.
3. Render reads `render.yaml` and provisions the web service automatically.
4. Once deployed, grab the `*.onrender.com` URL and add it to your LinkedIn, resume, CV, and GitHub profile README.

### Alternate hosts

- **Railway / Fly.io / Heroku-style**: `Procfile` is included.
- **Your own VPS**: standard Django + Gunicorn + Nginx setup works.

## Images to add

Before deploying, drop the following images into `static/img/`:

- `rishi.jpg` — headshot for the home page hero
- `projects/sourdough-hero.jpg`
- `projects/surgeonfish-hero.jpg`
- `projects/msa-hero.jpg`
- `projects/court-iq-hero.jpg`

The home page gracefully handles a missing headshot; project heroes will fallback to solid color panels.

## Tech

- Django 5, Python 3.12
- WhiteNoise for static file serving in production
- Gunicorn WSGI server
- Plain CSS (no framework) — editorial aesthetic with Fraunces, IBM Plex Sans, and JetBrains Mono

## License

© 2026 Rishi Gupta. Source code MIT; written content all rights reserved.
