# 🩸 Blood Bank Management System (Django)

A modern, end‑to‑end Blood Bank Management System built with **Django**. It streamlines donor onboarding, patient requests, and inventory tracking with role‑based access for **Admin**, **Donor**, and **Patient** users. Clean, mobile‑friendly UI with Django templates, forms, and robust server‑side validation.

> **Repo:** `https://github.com/harsh-dhakr/blood-bank-management-in-django`

---

## Table of Contents

* ✨ [Features](#-features)
* 🚀 [Tech Stack](#-tech-stack)
* 📁 [Project Structure](#-project-structure)
* ⚙️ [Prerequisites](#-prerequisites)
* 🛠️ [Setup Instructions](#-setup-instructions)

  * Backend (Django)
  * Database Setup
* ▶️ [Running the Application](#️-running-the-application)
* 🔌 [Routes / Endpoints](#-routes--endpoints)

  * Auth
  * Donor
  * Patient
  * Admin
* 🧪 [Testing](#-testing)
* 🐞 [Debugging Common Issues](#-debugging-common-issues)
* 🔑 [Environment Variables](#-environment-variables)
* 📮 [Postman Collection (Optional API)](#-postman-collection-optional-api)
* 🤝 [Contributing](#-contributing)
* 📄 [License](#-license)

---

## ✨ Features

### 🔐 Authentication & Profiles

* Sign up / Login for **Donors** and **Patients**.
* Admin manages users from Django Admin.
* Profile fields: name, email, phone, address, blood group, last donation date.

### 🧑‍🤝‍🧑 Donor Portal

* Create **Donation Requests** (health screening form).
* View donation history with statuses **Pending / Approved / Rejected**.

### 🧑‍⚕️ Patient Portal

* Create **Blood Requests** (blood group + units + urgency).
* Track request statuses and history.

### 🧮 Inventory Management

* Auto‑update stock on **approved** donations/requests.
* Dashboard cards by blood group (A+, A−, B+, B−, AB+, AB−, O+, O−).

### 🛡️ Admin Dashboard

* Approve/Reject **Donation** & **Blood** requests.
* Manage **Donors**, **Patients**, and **Inventory**.
* View global stats: total units, approved/pending counts, recent activity.

### 🎨 UI/UX

* Responsive Django templates with a clean, red/health‑theme.
* Toast/flash messages for user feedback.

> **Note:** If you’ve added extra features (email notifications/SMS, DRF APIs, pagination, search, etc.), feel free to extend this README—placeholders are included below.

---

## 🚀 Tech Stack

| Layer    | Tech                                                        |
| -------- | ----------------------------------------------------------- |
| Backend  | **Python 3.10+**, **Django 4.x**                            |
| Database | **SQLite** (dev) / **PostgreSQL** (prod optional)           |
| Auth     | Django auth, role‑based permissions                         |
| Forms    | Django Forms / ModelForms                                   |
| Admin    | Django Admin                                                |
| Optional | Django REST Framework (DRF) for APIs, Celery for emails/SMS |

---

## 📁 Project Structure

```text
blood-bank-management-in-django/
├─ hospital/                     # Django project
│  ├─ manage.py
│  ├─ hospital/                  # Project settings module
│  │  ├─ __init__.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  └─ wsgi.py
│  ├─ accounts/                  # Auth & profiles (Donor/Patient roles)
│  │  ├─ models.py
│  │  ├─ forms.py
│  │  ├─ views.py
│  │  └─ urls.py
│  ├─ donors/                    # Donation requests & history
│  ├─ patients/                  # Blood requests & history
│  ├─ inventory/                 # Stock management per blood group
│  ├─ templates/                 # HTML templates
│  ├─ static/                    # CSS/JS/images
│  └─ requirements.txt           # Python dependencies
└─ README.md
```

> *Your actual folders may vary; update the tree to match your code.*

---

## ⚙️ Prerequisites

* **Python 3.10+**
* **pip** & **virtualenv**
* **SQLite** (bundled) or **PostgreSQL 14+** (optional)
* **Git**

Optional (if you enable APIs/notifications):

* **Django REST Framework**
* **SMTP** account for email (Gmail/App Password recommended)

---

## 🛠️ Setup Instructions

### 1) Clone & enter project

```bash
git clone https://github.com/harsh-dhakr/blood-bank-management-in-django.git
cd blood-bank-management-in-django/hospital
```

### 2) Create & activate virtualenv

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3) Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install common packages:

```bash
pip install django==4.2.* psycopg2-binary python-dotenv
# Optional
pip install djangorestframework django-cors-headers
```

### 4) Configure environment variables

Create **.env** (same folder as `manage.py`):

```env
# Django
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

# Database (SQLite by default). For Postgres, uncomment below
# DATABASE_URL=postgres://postgres:password@localhost:5432/bloodbank

# Email (optional notifications)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

Then load these in `settings.py` (if not already):

```python
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
```

For Postgres, add:

```python
import dj_database_url
DATABASES = {
  'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}
```

### 5) Migrations & superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 6) (Optional) Seed demo data

Use Django Admin to add a few donors/patients and stock units, or create a custom management command later.

---

## ▶️ Running the Application

```bash
python manage.py runserver
```

App will be available at: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🔌 Routes / Endpoints

> **Note:** If you’re serving HTML views, these are page URLs. If you enable DRF, mirror them as `/api/...` endpoints.

### 🧭 Auth

* `GET /login/` – Login page
* `GET /signup/` – Choose role (Donor/Patient) and register
* `POST /logout/` – Logout
* `GET /profile/` – View/update profile

### 🩸 Donor

* `GET /donor/dashboard/` – Summary cards & quick links
* `GET|POST /donor/donate/` – Create donation request
* `GET /donor/donations/` – Donation history

### 🩺 Patient

* `GET /patient/dashboard/`
* `GET|POST /patient/request/` – Request blood units
* `GET /patient/requests/` – Request history

### 🛡️ Admin

* `GET /admin/` – Django Admin
* Approve/Reject **Donation Requests** → stock **adds** on approval
* Approve/Reject **Blood Requests** → stock **deducts** on approval

> **REST API (Optional):** If using DRF, expose `POST /api/donations/`, `POST /api/requests/`, `GET /api/inventory/`, etc., and secure with token/session auth.

---

## 🧪 Testing

```bash
# Run Django tests
python manage.py test
```

Recommended areas to test:

* Models: stock adjustments per approval
* Views/Forms: validation, permissions per role
* Signals/Services: inventory recalculation

---

## 🐞 Debugging Common Issues

**Migrations errors**

```bash
# Reset local db (dev only!)
rm -f db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations && python manage.py migrate
```

**Static files not loading**

```bash
python manage.py collectstatic
```

Ensure `STATIC_URL` and `STATICFILES_DIRS`/`STATIC_ROOT` are configured.

**Login redirects wrong**
Set in `settings.py`:

```python
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = '/login/'
```

**CSRF issues on POST**
Ensure you render `{% csrf_token %}` in every `<form>` block.

**Email not sending**
Use an **App Password** for Gmail, and verify `EMAIL_*` settings.

---

## 🔑 Environment Variables

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
# DATABASE_URL=postgres://postgres:password@localhost:5432/bloodbank
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

---

## 📮 Postman Collection (Optional API)

If you add DRF:

* Import `postman/BloodBank.postman_collection.json` and `postman/BloodBank.postman_environment.json`.
* Set environment vars: `baseUrl`, `token`.

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "feat: add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 📌 Roadmap (suggested)

* [ ] Email/SMS notifications for approvals
* [ ] DRF APIs + React/Vue admin (optional)
* [ ] Search & filters (by blood group, city)
* [ ] Export CSV/PDF reports
* [ ] Pagination & caching for lists
