# Django Middleware for Authorization: A Clear, Practical Guide

This guide explains how to use Django's middleware for authorization. It's a powerful tool for enforcing site-wide rules.

---

## **1. What is Middleware?**

Middleware is a framework of hooks into Django’s request/response processing. It’s a light, low-level plugin system for globally altering Django’s input or output.

Think of it as a series of layers that every request must pass through on its way to the view, and then again on its way out to the browser.

**The Flow:**
```
Browser Request -> Middleware Layer 1 -> Middleware Layer 2 -> ... -> View -> ... -> Middleware Layer 2 -> Middleware Layer 1 -> Browser Response
```

It's ideal for tasks that need to be applied **globally**, such as:
*   Authentication checks
*   Enforcing site-wide access rules
*   Logging
*   Setting headers on every response

---

## **2. When to Use Middleware for Authorization (and When Not To)**

Middleware is powerful, but it's not the right tool for every job. It's crucial to know when to use it.

| Use Middleware For 👍                                       | Don't Use Middleware For 👎                               |
| ----------------------------------------------------------- | --------------------------------------------------------- |
| **Global, site-wide rules** (e.g., all users must be logged in) | **Object-level permissions** (e.g., `post.author == user`)  |
| **URL-based rules** (e.g., `/staff/` requires `is_staff` flag)  | **Complex, view-specific business logic**                 |
| **Enforcing account status** (e.g., user must have a verified email) | **Heavy database queries** (runs on almost every request) |
| **Organization/Tenant access** in multi-tenant applications     | Logic that is better handled by a decorator or mixin      |

**Key takeaway:** Use middleware for broad, cross-cutting concerns. Use decorators, mixins, or in-view logic for specific, fine-grained control.

---

## **3. How to Write an Authorization Middleware**

Creating middleware is straightforward.

**Step 1: Create the file**
Best practice is to put it in a `middleware.py` file inside one of your apps.
`yourapp/middleware.py`

**Step 2: Write the class**
A middleware can be a simple class with `__init__` and `__call__` methods.

```python
# yourapp/middleware.py
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseForbidden

class MyAuthMiddleware:
    def __init__(self, get_response):
        # This is one-time configuration and initialization.
        self.get_response = get_response

    def __call__(self, request):
        # Code here runs BEFORE the view is called.

        # Example: A simple check
        if not request.user.is_authenticated:
            # Do something, like redirect to login
            pass

        response = self.get_response(request)

        # Code here runs AFTER the view is called.

        return response
```

**Step 3: Register it in `settings.py`**
Add the full path to your middleware class to the `MIDDLEWARE` list. **The order matters!**

```python
# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # ... other default middleware
    'yourapp.middleware.MyAuthMiddleware', # Add your middleware here
    # ...
]
```

**Important Note on Ordering:** Middleware is processed from top to bottom. Place your custom auth middleware after Django's `SessionMiddleware` and `AuthenticationMiddleware` so that `request.user` is available.

---

## **4. Practical Examples**

### **Example 1: Global "Login Required"**
Force login for all pages except a few public ones (like login, signup, and the admin panel).

```python
# yourapp/middleware.py
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # Define paths that don't require login
        self.public_paths = [reverse('login'), reverse('signup')]
        self.public_prefixes = ['/admin/']

    def __call__(self, request):
        # Check if the path is public
        is_public_path = any(request.path.startswith(prefix) for prefix in self.public_prefixes)
        
        if not request.user.is_authenticated and request.path not in self.public_paths and not is_public_path:
            return redirect(reverse('login'))

        response = self.get_response(request)
        return response
```

### **Example 2: Role-Based URL Restriction**
Restrict access to any URL starting with `/staff/` to users with the `is_staff` flag.

```python
# yourapp/middleware.py
from django.http import HttpResponseForbidden

class StaffOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/staff/'):
            if not request.user.is_staff:
                return HttpResponseForbidden("Access denied. Staff only.")
        
        response = self.get_response(request)
        return response
```

### **Example 3: Multi-Tenant Organization Check (Advanced)**
In a SaaS application, you often need to ensure a user belongs to the organization they are trying to access. This is a perfect use case for middleware.

Let's assume the URL is like `/org/{org_slug}/dashboard/`.

```python
# yourapp/middleware.py
from django.http import HttpResponseForbidden

# Assume you have a way to get the current organization from the request,
# for example, from a URL resolver match or a subdomain.
def get_organization_slug(request):
    return request.resolver_match.kwargs.get('org_slug')

class OrganizationAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        org_slug = get_organization_slug(request)

        if org_slug and request.user.is_authenticated:
            # Check if the user is a member of the organization they are trying to access.
            # This is a hypothetical check; your logic will depend on your models.
            if not request.user.organizations.filter(slug=org_slug).exists():
                return HttpResponseForbidden("You do not have access to this organization.")
        
        response = self.get_response(request)
        return response
```

---

## **5. Common Mistakes to Avoid**

*   **Heavy Database Queries:** Middleware runs on nearly every request. A heavy query will slow down your entire site. Cache results if you must perform a query.
*   **Object-Level Logic:** Do not check for object ownership in middleware. It's inefficient and belongs in the view.
*   **Incorrect Order:** Placing your middleware before `AuthenticationMiddleware` means `request.user` won't be available.
*   **Forgetting Exclusions:** Forgetting to exclude login/signup pages from a login-required middleware can cause an infinite redirect loop.

---

## **Summary: The Right Tool for the Right Job**

| Authorization Tool       | Best For...                               |
| ------------------------ | ----------------------------------------- |
| **Middleware**           | **Global**, URL-based, and cross-cutting rules. |
| **Decorators/Mixins**    | **View-level** rules and permission checks. |
| **In-View Logic**        | **Object-level** and business logic checks. |
| **Groups & Permissions** | Defining and managing **roles**.          |