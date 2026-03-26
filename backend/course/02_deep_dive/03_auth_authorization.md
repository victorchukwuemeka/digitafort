# Django Authorization: A Clear, Practical Guide

This guide provides a simple, step-by-step explanation of Django's authorization system. No heavy theory, just what you need for real-world projects.

---

## **1. The Two A's: Authentication vs. Authorization**

First, let's clarify the two core concepts.

### **Authentication: "Who are you?"**
This is the process of verifying a user's identity.
* **Examples:** Logging in, logging out, signing up.
* **Django's Role:** Django handles this with its session and authentication framework. The `request.user` object is the result of successful authentication.

### **Authorization: "What can you do?"**
This is the process of checking if an authenticated user has the necessary permissions to perform an action.
* **Examples:** Can this user create a post? Can they delete another user's comment? Are they an admin?
* **Django's Role:** Django provides a powerful, built-in authorization framework based on permissions, groups, and user flags.

**Key Idea:** Authentication comes first. You can't authorize someone you don't know.

---

## **2. The Core Pillars of Django Authorization**

Django's authorization system is built on three main pillars.

### **Pillar 1: User Flags (`is_staff`, `is_superuser`)**

The built-in `User` model has special flags for simple, powerful authorization:

```python
from django.contrib.auth.models import User
```

* **`is_staff` (boolean):** Can this user access the Django admin site? This is perfect for giving trusted users access to your site's backend without giving them god-mode.
* **`is_superuser` (boolean):** Does this user have all permissions, bypassing all checks? Use this only for the most trusted administrators. A superuser is implicitly also `is_staff`.

### **Pillar 2: Permissions**

Permissions are granular rules that grant a specific capability. The format is `app_label.action_modelname`.

* **Examples:**
    * `blog.add_post`
    * `blog.change_post`
    * `blog.delete_post`

When you create a Django model, it automatically generates `add`, `change`, `delete`, and `view` permissions.

**Checking for a permission is simple:**
```python
if request.user.has_perm('blog.add_post'):
    # User is allowed to add a post
else:
    # User is not allowed, return a 403 Forbidden response
```

### **Pillar 3: Groups**

Assigning permissions to users one-by-one is tedious and error-prone. **Groups** solve this by letting you create roles.

* **Example Roles:** "Editors", "Moderators", "Premium Members"

**How it works:**
1. You create a `Group` (e.g., "Editors").
2. You assign `Permissions` to that group (e.g., `blog.change_post`).
3. You add a `User` to the group.

Now, that user has all the permissions of the "Editors" group.

```python
from django.contrib.auth.models import Group

# Check if a user is in the 'Editor' group
if request.user.groups.filter(name='Editor').exists():
    # This user is an editor
```

---

## **3. Protecting Your Views: Putting It All Together**

Now, let's see how to protect your code.

### **Always Start with Authentication**

Before checking *what* a user can do, you must ensure they are logged in.

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_protected_view(request):
    # This code will only run if the user is authenticated.
    # Guests will be redirected to the login page.
```

### **Function-Based Views: The `@permission_required` Decorator**

The easiest way to protect a function-based view is with the `@permission_required` decorator.

```python
from django.contrib.auth.decorators import permission_required

@login_required
@permission_required('blog.add_post', raise_exception=True)
def create_post(request):
    # This view is only accessible to logged-in users with the 'add_post' permission.
    # If the check fails, it will raise a 403 Forbidden error.
```
*Note: Stacking decorators is common. Always put `@login_required` first.*

### **Class-Based Views: The `PermissionRequiredMixin`**

For class-based views, Django provides a mixin that does the same thing.

```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView
from .models import Post

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    permission_required = 'blog.add_post'
    # ... other view configuration
```

### **Object-Level Permissions: Ownership and Business Logic**

Sometimes, a simple permission isn't enough. For example, a user should only be able to edit *their own* post, not someone else's.

This is **business-logic authorization** or **object-level permission**. You write this logic directly in your view.

```python
from django.http import HttpResponseForbidden

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    # Is the logged-in user the author of this specific post?
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")

    # ... proceed with the view logic
```

---

## **4. Advanced Scenarios**

### **Django REST Framework (DRF)**

When building APIs, DRF has its own excellent permission system.

```python
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.views import APIView

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class PostDetailView(APIView):
    permission_classes = [IsAuthenticated, IsOwner] # A list of permissions
    # ...
```

### **Customizing the Admin**

You can control behavior within the Django admin. For example, only superusers should be able to delete posts.

`admin.py`:
```python
from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        # Only allow superusers to delete posts
        return request.user.is_superuser
```

---

## **Summary: A Mental Checklist for Authorization**

When a user tries to do something, think through this checklist:

1.  **Is the user authenticated?** (Are they logged in?)
    *   If not, redirect to login.
2.  **Is this a special area?** (e.g., admin panel)
    *   If so, check `is_staff` or `is_superuser`.
3.  **Does the user have the required role or permission?**
    *   Check `user.has_perm()` or group membership.
4.  **Is there a business rule to check?** (e.g., ownership)
    *   Perform the object-level check (e.g., `post.author == request.user`).

If the answer is **YES** to all relevant questions, the user is authorized.

---

## **Practice Makes Perfect**

*   Create a blog app.
*   Create an "Editors" group and give them `change_post` permissions.
*   Restrict post deletion to only `is_superuser`.
*   Implement the "author can edit their own post" logic.