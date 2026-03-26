# Lesson 2: Setting Up Your Development Environment

To begin building with Django, you need a clean and organized development environment. This lesson will guide you through installing Python, setting up virtual environments, and installing Django.

---

### 1. Install Python
Django is a Python framework, so you need Python installed (version 3.10+ recommended).
*   **Check Python version:** `python --version` (or `python3 --version`)

### 2. Virtual Environments: Why and How
A virtual environment is an isolated space for a Python project. It ensures that dependencies for one project don't conflict with another.

*   **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
*   **Activate it:**
    *   **Windows:** `venv\Scripts\activate`
    *   **Mac/Linux:** `source venv/bin/activate`

### 3. Install Django
Once activated, install Django using `pip`:
```bash
pip install django
```
Verify the installation:
```bash
django-admin --version
```

### 4. Code Editor (IDE)
We recommend using **Visual Studio Code (VS Code)** with the **Python** and **Django** extensions for the best experience.

### 5. Database (SQLite)
By default, Django uses **SQLite**, which is a file-based database that requires no extra setup. It's perfect for learning and small projects. In later modules, we'll switch to **PostgreSQL** for production.

---
**Summary:**
*   Python 3.10+
*   Virtual environments keep your projects clean.
*   `pip install django` is your entry point.
