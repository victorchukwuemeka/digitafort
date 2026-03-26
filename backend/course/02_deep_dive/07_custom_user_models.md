# Lesson 7: Custom User Models & User Profiles

By default, Django comes with a built-in `User` model. However, for most professional projects, it's highly recommended to use a **Custom User Model** from the very beginning. This lesson will show you why and how.

---

### 1. Why a Custom User Model?
*   **Flexibility:** You can add extra fields (e.g., `profile_picture`, `subscription_level`, `bio`).
*   **Authentication:** You can change how users log in (e.g., using `email` instead of `username`).
*   **Future-Proofing:** Changing the user model *after* you have data in the database is very difficult.

### 2. The Golden Rule: Start Early
Always define your custom user model **before** you run your first migration (`python manage.py migrate`).

### 3. Creating a Custom User Model
The best way to do this is to inherit from `AbstractUser`.

In `users/models.py` (assuming you created a 'users' app):
```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add your custom fields here
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
    is_premium = models.BooleanField(default=False)
```

### 4. Registering Your Custom User Model
You must tell Django to use your new model for authentication.

In `settings.py`:
```python
AUTH_USER_MODEL = 'users.CustomUser'
```

### 5. Using the Custom User Model in Your Project
When you need to refer to the user model in other apps, **never** import the `CustomUser` class directly. Instead, use `get_user_model()`.

In `blog/models.py`:
```python
from django.conf import settings
from django.db import models

class Post(models.Model):
    # Use settings.AUTH_USER_MODEL for foreign keys
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # ...
```

---
**Summary:**
*   Start every project with a custom user model.
*   Inherit from `AbstractUser` for a smooth transition.
*   Always use `get_user_model()` or `settings.AUTH_USER_MODEL` to refer to users.
*   Don't forget to update `settings.py`!
