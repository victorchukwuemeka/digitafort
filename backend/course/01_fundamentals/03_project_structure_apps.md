# Lesson 3: Project Structure & The "App" Philosophy

Django has a unique and powerful way of organizing code: the **Project** and **App** philosophy. This lesson explains the difference and shows you how to navigate a standard Django directory.

---

### 1. Project vs. App: The Core Difference

*   **A Project:** Think of this as the "container" for your entire website. It contains the core configuration (database settings, main URL routing, installed apps). You create one project per website.
*   **An App:** This is a "module" that performs a specific function (e.g., a "Blog", a "Store", a "User Profile"). You can have many apps in one project.

**The Golden Rule:** A project can have many apps. An app can be reused across different projects.

### 2. Creating Your First Project

Run this command to create a project named `mywebsite`:
```bash
django-admin startproject mywebsite
cd mywebsite
```

### 3. Creating Your First App

Inside your project folder, create a new app named `blog`:
```bash
python manage.py startapp blog
```

### 4. Anatomy of a Django Project

```
mywebsite/
├── manage.py            # Your command-line tool for the project
└── mywebsite/           # Core project settings folder
    ├── settings.py      # Database, apps, static files, etc.
    ├── urls.py          # Main URL dispatcher
    └── wsgi.py/asgi.py  # Server interface for deployment
blog/                    # Your app folder
├── models.py            # Database structure
├── views.py             # Logic for processing requests
├── admin.py             # Customization for the admin interface
├── apps.py              # App-specific configuration
└── migrations/          # History of database changes
```

### 5. Registering Your App
For Django to recognize your new app, you must add it to the `INSTALLED_APPS` list in `settings.py`:

```python
# mywebsite/settings.py
INSTALLED_APPS = [
    # ... default apps ...
    'blog',
]
```

---
**Summary:**
*   Project = Website; App = Feature.
*   Always register your apps in `settings.py`.
*   `manage.py` is your primary tool for interacting with Django.
