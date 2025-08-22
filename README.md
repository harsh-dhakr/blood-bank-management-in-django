# 🩸 Blood Bank Management System (Django)

A modern, end‑to‑end Blood Bank Management System built with **Django**. It streamlines donor onboarding, patient requests, and inventory tracking with role‑based access for **Admin**, **Donor**, and **Patient** users. Clean, mobile‑friendly UI with Django templates, forms, and robust server‑side validation.

> **Repo:** `https://github.com/harsh-dhakr/blood-bank-management-in-django`

---


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
│  ├              
│  ├─ templates/                 # HTML templates
│  ├─ static/                    # CSS/JS/images
│  └─ requirements.txt           # Python dependencies
└─ README.md
```


