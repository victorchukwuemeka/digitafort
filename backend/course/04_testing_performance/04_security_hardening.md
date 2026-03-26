# Lesson 4: Security Hardening for Production

Django is designed to be secure by default. However, there are many steps you must take to ensure your application is truly production-ready and protected against modern web threats.

---

### 1. The `SECRET_KEY`
The `SECRET_KEY` is the heart of Django's security. It's used for generating sessions, CSRF tokens, and hashing passwords.
*   **NEVER** commit your `SECRET_KEY` to version control.
*   Use environment variables to store it in production.

### 2. Django's Deployment Checklist
Django provides a built-in command to check your settings for common security issues.

```bash
python manage.py check --deploy
```

### 3. Essential Security Settings
*   **`DEBUG = False`:** Never run with `DEBUG = True` in production. It exposes sensitive information about your code and environment.
*   **`ALLOWED_HOSTS`:** Explicitly list the domain names your site is allowed to serve.
*   **`SECURE_SSL_REDIRECT = True`:** Force all requests to use HTTPS.
*   **`SESSION_COOKIE_SECURE = True`:** Only send session cookies over HTTPS.
*   **`CSRF_COOKIE_SECURE = True`:** Only send CSRF cookies over HTTPS.

### 4. Protecting Against Common Attacks
*   **SQL Injection:** Django's ORM automatically handles query parameterization, protecting you against SQL injection. Avoid writing raw SQL queries.
*   **XSS (Cross-Site Scripting):** Django's template engine automatically escapes all HTML content. Use the `|safe` tag only when you are absolutely sure of the content's source.
*   **CSRF (Cross-Site Request Forgery):** Django requires a CSRF token for every `POST` request. Always include `{% csrf_token %}` in your forms.

### 5. Managing Environment Variables
Use a library like `python-dotenv` or `django-environ` to manage sensitive settings like database credentials and API keys.

In your `.env` file:
```text
SECRET_KEY=your-super-secret-key
DATABASE_URL=postgres://user:pass@localhost:5432/dbname
DEBUG=False
```

---
**Summary:**
*   Security is an ongoing process, not a one-time task.
*   Always use `python manage.py check --deploy`.
*   Keep your `SECRET_KEY` secret.
*   Force HTTPS for everything in production.
