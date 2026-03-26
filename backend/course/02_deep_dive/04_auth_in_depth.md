# Module 1: Foundations: Web, Django & Authorization

## Lesson 3: Authentication & Authorization in Depth

Building secure web applications requires a robust understanding of how to manage user identities and control their access to resources. In this lesson, we'll dive deep into Django's powerful built-in authentication and authorization system, expanding on the concepts introduced in `authorization.md`.

---

### 1. Authentication vs. Authorization Revisited

Before we delve into Django's specifics, let's reinforce these two core, distinct concepts:

*   **Authentication (AuthN): "Who are you?"**
    *   This is the process of verifying a user's identity. When you log in with a username and password, you are authenticating yourself.
    *   **Django's Role:** Django provides a complete authentication system including user accounts, groups, permissions, and session-based authentication. The `request.user` object is the result of a successful authentication.

*   **Authorization (AuthZ): "What can you do?"**
    *   This is the process of determining if an authenticated user has the necessary permissions to perform a specific action or access a particular resource.
    *   **Django's Role:** Django's authorization framework is tightly integrated with its authentication system, allowing you to define granular permissions and assign them to users or groups.

**Key Idea:** Authentication *always* comes before authorization. You cannot decide what someone can do until you know who they are.

---

### 2. Django's Built-in Authentication System

Django comes with a full-featured authentication system right out of the box, located in `django.contrib.auth`.

#### The `User` Model

The heart of Django's authentication is the `User` model (`django.contrib.auth.models.User`). This model stores essential user information:

*   `username`
*   `password` (hashed, of course!)
*   `email`
*   `first_name`, `last_name`
*   `is_active` (can the user log in?)
*   `is_staff` (can the user access the admin site?)
*   `is_superuser` (does the user have all permissions?)
*   `date_joined`, `last_login`

You can extend this `User` model with a [Custom User Model](https://docs.djangoproject.com/en/stable/topics/auth/customizing/#substituting-a-custom-user-model) if you need more fields, but the default often suffices.

#### Authentication Flow

1.  **Login:** A user submits credentials (e.g., username/password).
2.  **`authenticate()`:** Django's `authenticate()` function (from `django.contrib.auth`) attempts to verify these credentials using configured authentication backends.
3.  **`login()`:** If `authenticate()` succeeds, `login(request, user)` creates a session for the user, storing their ID in the session. This links the user to subsequent requests.
4.  **`request.user`:** On each subsequent request, the `AuthenticationMiddleware` retrieves the user ID from the session and populates `request.user` with the corresponding `User` object. If no user is logged in, `request.user` will be an `AnonymousUser` object.
5.  **Logout:** `logout(request)` clears the user's session data and logs them out.

**Important:** The `AuthenticationMiddleware` must be enabled in `settings.py` for `request.user` to be available. (It's usually there by default).

```python
# settings.py
MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # This one!
    # ...
]
```

---

### 3. Django's Authorization System: Permissions and Groups

Django's authorization system is built on three core pillars, as outlined in `authorization.md`:

#### Pillar 1: User Flags (`is_staff`, `is_superuser`)

These are simple boolean fields on the `User` model:

*   **`is_staff`:** If `True`, the user can log into the Django admin site. It doesn't automatically grant any permissions beyond admin access.
*   **`is_superuser`:** If `True`, the user has all permissions without explicitly being granted them. A superuser is implicitly also a staff member. Use this sparingly for administrators who need full control.

#### Pillar 2: Permissions

Permissions are granular rules that define what actions a user can take on a specific model.

*   **Automatic Permissions:** When you define a `Model` in `models.py`, Django automatically creates four default permissions for it:
    *   `app_label.add_model_name` (e.g., `blog.add_post`)
    *   `app_label.change_model_name` (e.g., `blog.change_post`)
    *   `app_label.delete_model_name` (e.g., `blog.delete_post`)
    *   `app_label.view_model_name` (e.g., `blog.view_post`)
*   **Custom Permissions:** You can define your own custom permissions in the `Meta` class of your model.

    ```python
    # blog/models.py
    class Post(models.Model):
        # ... fields ...
        class Meta:
            permissions = [
                ("can_publish_post", "Can publish a post"),
                ("can_moderate_comments", "Can moderate comments"),
            ]
    ```

#### Checking Permissions

You can check if a user has a specific permission using the `has_perm()` method of the `User` object:

```python
if request.user.has_perm('blog.add_post'):
    # User can add a post
    pass
else:
    # User cannot add a post
    from django.http import HttpResponseForbidden
    return HttpResponseForbidden("You are not authorized to add posts.")
```

#### Pillar 3: Groups

Managing permissions individually for each user can quickly become cumbersome. **Groups** allow you to bundle permissions and then assign users to those groups, simplifying user management.

*   **How it works:**
    1.  Create a `Group` (e.g., "Editors").
    2.  Assign `Permissions` to that `Group` (e.g., `blog.change_post`, `blog.view_post`).
    3.  Add `User` objects to the `Group`. Any user in the "Editors" group will then inherit all permissions assigned to that group.

*   **Checking Group Membership:**

    ```python
    if request.user.groups.filter(name='Editor').exists():
        # This user is an editor
        pass
    ```

---

### 4. Protecting Your Views: Decorators and Mixins

Django provides convenient ways to enforce authentication and authorization directly on your views.

#### a. `@login_required` Decorator (Function-Based Views)

Ensures that a user is authenticated before they can access the view. If not, they are redirected to the login page (or `settings.LOGIN_URL`).

```python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')
```

#### b. `@permission_required` Decorator (Function-Based Views)

Ensures the authenticated user has a specific permission. If not, it redirects to `settings.LOGIN_URL` (if `raise_exception=False`) or raises a `PermissionDenied` (HTTP 403 Forbidden) exception (if `raise_exception=True`).

```python
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@login_required # Always put login_required first!
@permission_required('blog.add_post', raise_exception=True)
def create_post_view(request):
    # Only accessible to logged-in users with 'blog.add_post' permission
    return render(request, 'create_post.html')
```
You can pass a list of permissions: `permission_required(['blog.add_post', 'blog.change_post'])`. By default, the user must have *all* listed permissions. Use `perm_required_all=False` if they only need *any* of them.

#### c. `LoginRequiredMixin` (Class-Based Views)

The class-based equivalent of `@login_required`.

```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Post

class MyProtectedListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'protected_list.html'
```

#### d. `PermissionRequiredMixin` (Class-Based Views)

The class-based equivalent of `@permission_required`.

```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView
from .models import Post

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    permission_required = 'blog.add_post' # Can also be a tuple: ('blog.add_post', 'blog.change_post')
    # If permission_required is a tuple, by default, the user must have ALL of them.
    # Set `raise_exception = True` for a 403 Forbidden response.
    # Set `permission_denied_message` for a custom message.
```

---

### 5. Object-Level Permissions: Business Logic

While permissions (`has_perm`) are great for broad access control (e.g., "Can this user change *any* post?"), they often fall short when you need to check access to a *specific instance* of an object (e.g., "Can this user change *this particular* post, which they own?"). This is where **object-level permissions** or **business logic authorization** comes in.

This logic is typically implemented directly within your view or API endpoint.

```python
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def edit_own_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Core object-level check: Is the logged-in user the author of this post?
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post as you are not the author.")

    # If the user IS the author, proceed with editing logic
    if request.method == 'POST':
        # ... process form ...
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_detail', pk=post.pk) # Assuming a post_detail view
    
    return render(request, 'edit_post.html', {'post': post})
```
For more complex object-level permission requirements, libraries like [Django Guardian](https://django-guardian.readthedocs.io/) can provide a more generic framework, but for many cases, direct in-view logic is perfectly acceptable.

---

### Conclusion

Django's authentication and authorization system is robust and flexible. By understanding the `User` model, permissions, groups, and how to use decorators and mixins, you can effectively control who can access what in your application. Object-level permissions allow you to implement fine-grained access based on specific data instances. In the next lesson, we'll see how Django Middleware can be used to enforce even broader, site-wide authorization rules.

---
**Further Reading (Optional):**
*   [Django Authentication and Authorization](https://docs.djangoproject.com/en/stable/topics/auth/)
*   [Django Guardian (for advanced object-level permissions)](https://django-guardian.readthedocs.io/)