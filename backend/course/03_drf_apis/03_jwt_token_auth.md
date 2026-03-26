# Lesson 3: Securing Your API: JWT & Token Authentication

By default, Django uses session-based authentication, which works great for web browsers. However, for APIs being used by mobile apps or single-page applications (like React), **Token-Based Authentication** or **JSON Web Tokens (JWT)** is the standard.

---

### 1. Simple Token Authentication
DRF has a built-in token authentication system. When a user logs in, the server generates a unique, long-lasting token. The client then includes this token in the header of every subsequent request.

In `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'rest_framework.authtoken',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}
```

### 2. Introduction to JWT
**JWT (JSON Web Token)** is a more advanced and scalable alternative. Unlike simple tokens, JWTs are self-contained and don't need to be stored in the database.

*   **Access Token:** Short-lived (e.g., 5-60 minutes).
*   **Refresh Token:** Long-lived (e.g., days or weeks).

We'll use the popular `djangorestframework-simplejwt` library.

### 3. Setting Up JWT Authentication
```bash
pip install djangorestframework-simplejwt
```

In `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
```

### 4. JWT Endpoints
In `mywebsite/urls.py`:
```python
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

### 5. Using Permissions with JWT
You can now protect your API views using DRF's built-in permission classes:

```python
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] # Only logged-in users with a valid JWT
    # ...
```

---
**Summary:**
*   Tokens are standard for modern APIs.
*   JWT is a powerful, stateless way to handle authentication.
*   `simplejwt` is the easiest way to add JWT to your Django project.
*   Protect your views using `permission_classes`.
