# CreatorFlow 🚀

CreatorFlow is a Django-based web platform designed to help creators manage knowledge, transform ideas into content drafts, schedule posts, and automate publishing to social media platforms.

The system combines **knowledge management**, **content scheduling**, and **automation** into one productivity tool.

---

# 📊 Core Modules

## Knowledge Management
Store and manage content ideas.

Fields:
- title
- content
- tags
- created_at

## Content Draft
Convert knowledge into social media posts.

Fields:
- post_content
- platform
- media
- hashtags

## Post Scheduler
Schedule posts for publishing.

Fields:
- platform
- scheduled_time
- status

## Automation Engine
Automates posting using Selenium.

---

# 📌 Features

- Knowledge Management - store ideas, notes, and content drafts
- Content Drafting - convert ideas into social media posts
- Post Scheduling - schedule posts for a specific time
- Automation Engine - automatically publish posts using Selenium
- Tagging System - organize ideas using tags
- Post Status Tracking - Draft / Scheduled / Published

---

# 🏗️ System Architecture

User -> Django Web App -> Database  
                     -> Scheduler  
                     -> Automation Engine  
                     -> Social Media Platforms

---

# 🛠️ Tech Stack

Backend
- Django
- Django REST Framework

Automation
- Selenium
- WebDriver Manager

Database
- PostgreSQL / SQLite

Task Scheduling
- Celery
- Redis

Environment Management
- Python Dotenv

---

# ⚙️ Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd Creator-Knowledge-Social-Automation-Hub
```

2. Create and activate a virtual environment:
```bash
python -m venv myvenv
# Windows
myvenv\Scripts\activate
# macOS/Linux
source myvenv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables in a `.env` file:
```env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
REDIS_URL=redis://localhost:6379/0
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the Django development server:
```bash
python manage.py runserver
```

7. Start Celery worker:
```bash
celery -A <your_django_project_name> worker --loglevel=info
```

8. (Optional) Start Celery beat:
```bash
celery -A <your_django_project_name> beat --loglevel=info
```

---

# 📂 Project Structure

```text
Creator-Knowledge-Social-Automation-Hub/
|-- README.md
|-- requirements.txt
|-- manage.py
|-- <django_project>/
|   |-- settings.py
|   |-- urls.py
|   `-- celery.py
|-- apps/
|   |-- knowledge/
|   |-- drafts/
|   |-- scheduler/
|   `-- automation/
`-- .env
```

---

# 🚀 Future Improvements

- AI generated post suggestions
- Multi platform support (LinkedIn, X, Instagram)
- Analytics dashboard
- Calendar view for scheduled posts
- OAuth login for social media accounts

---

# 🎯 Purpose

This project demonstrates:

- Backend architecture using Django
- Automation using Selenium
- Task scheduling systems
- Database design for content management

---

# 👨‍💻 Author

Shivam Kumar Dubey

GitHub  
https://github.com/shivamdubey023

LinkedIn  
https://www.linkedin.com/in/shivam-kumar-dubey-970a87248
