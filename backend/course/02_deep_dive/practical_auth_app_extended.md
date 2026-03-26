# Module 1: Foundations: Web, Django & Authorization

## Practical: Build and Secure a Basic Django Authorization App

This practical guide brings together all the concepts from Module 1 into a hands-on project. We'll build a simplified blog application, focusing on implementing Django's authentication, authorization, and middleware features to control user access. This practical will closely follow and expand upon the `mini.md` tutorial you were provided.

---

### Project Goal

We will create a blog application where:
*   Users can log in and view posts.
*   Users can create posts.
*   Users can **only edit their own** posts.
*   A special **"Editor" group** can edit *any* post.
*   Only **"Admins" (superusers)** can delete posts.
*   A custom middleware will ensure that **only logged-in users** can access the main blog content, redirecting guests to the login page.

---

### Prerequisites

*   Python 3.8+ and `pip` installed.
*   A basic understanding of the command line.
*   It's highly recommended to use a **virtual environment**. If you haven't already:
    ```bash
    python -m venv venv
    # On macOS/Linux:
    source venv/bin/activate
    # On Windows:
    .\venv\Scripts\activate
    ```

---

### Step 1: Project Setup

Let's start by setting up our Django project and the `blog` app.

1.  **Install Django:**
    ```bash
    pip install Django~=4.0 # Install a compatible Django version
    ```
2.  **Create the Project:**
    ```bash
    django-admin startproject auth_project
    cd auth_project
    ```
3.  **Create the Blog App:**
    ```bash
    python manage.py startapp blog
    ```
4.  **Register the `blog` app:**
    Open `auth_project/settings.py` and add `'blog'` to `INSTALLED_APPS`.

    ```python
    # auth_project/settings.py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'blog', # Our new app
    ]
    ```
5.  **Configure Login/Logout URLs:**
    Add these lines at the bottom of `auth_project/settings.py`. These URLs will be used by Django's built-in authentication system.

    ```python
    # auth_project/settings.py
    # ...
    LOGIN_REDIRECT_URL = '/'
    LOGOUT_REDIRECT_URL = '/accounts/login/' # Ensure this points to your login view
    LOGIN_URL = '/accounts/login/' # Explicitly define login URL for middleware/decorators
    ```

---

### Step 2: Define the `Post` Model

Now, let's define our `Post` model in `blog/models.py`. This model will link each post to a `User` (the author).

```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User # Django's built-in User model

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] # Order posts by newest first

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', args=[str(self.id)]) # Will be used after post creation
```

#### Apply Migrations

Generate and apply the database migrations for your new model.

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### Step 3: Create Users and Groups

We need different types of users and a group to test our authorization logic.

1.  **Create a Superuser (Admin):** This user will have all permissions.
    ```bash
    python manage.py createsuperuser
    # Follow the prompts to create your admin user (e.g., username: admin, password: password123)
    ```
2.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```
3.  **Create an "Editor" Group:**
    *   Navigate to the Django admin panel: `http://127.0.0.1:8000/admin/`
    *   Log in with your superuser account.
    *   Go to **Groups** -> **Add Group**.
    *   Name the group `Editor`.
    *   In the "Choose permissions" box, find the `blog | post` permissions. Assign the `Can change post` and `Can view post` permissions to this group. Save the group.
4.  **Create Normal Users:**
    *   In the admin panel, go to **Users** -> **Add User**.
    *   Create a "normaluser" (e.g., username: user, password: password123). Do not give them staff or superuser status, and do not assign to any group.
    *   Create an "editoruser" (e.g., username: editor, password: password123). Assign this user to the `Editor` group. Do not give them staff or superuser status.

---

### Step 4: Define Views with Authorization Logic

Now, let's implement our views in `blog/views.py`, incorporating the authorization checks we learned.

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin # For CBVs
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # Used with reverse_lazy for class-based views
from .models import Post
from .forms import PostForm # We will create this form next

# Function-based view example for creating a post (can be used if preferred)
@login_required
def create_post_fbv(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user # Set the current logged-in user as author
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form, 'page_title': 'Create New Post'})


# Class-based views for better structure and reusability
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts' # Name of the list in the template

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list') # Redirect after successful creation

    def form_valid(self, form):
        form.instance.author = self.request.user # Automatically set the author
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Create New Post'
        return context

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        is_author = post.author == request.user
        is_editor = request.user.groups.filter(name='Editor').exists()
        
        # Object-level permission: Only author OR editor can update
        if not (is_author or is_editor):
            return HttpResponseForbidden("You do not have permission to edit this post.")
        
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Edit Post'
        return context


class PostDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
    permission_required = 'blog.delete_post' # Requires the 'Can delete post' permission

    def has_permission(self):
        # Additional check: only superusers can delete posts (from mini.md example)
        # This overrides default behavior of PermissionRequiredMixin slightly
        return super().has_permission() and self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Delete Post'
        return context

# A simple "About Us" page for public access testing
def about_view(request):
    return render(request, 'blog/about.html')
```

#### Create `blog/forms.py`

Django forms simplify handling input.

```python
# blog/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] # We don't include 'author' as it's set automatically
```

---

### Step 5: Configure URLs

Now, let's wire up these views in `blog/urls.py` and the main `auth_project/urls.py`.

#### Create `blog/urls.py`

```python
# blog/urls.py
from django.urls import path
from .views import (
    PostListView, PostDetailView, PostCreateView,
    PostUpdateView, PostDeleteView, about_view, create_post_fbv # Include FBV if you want to test it
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    # path('post/new-fbv/', create_post_fbv, name='post_create_fbv'), # Alternative FBV for create
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('about/', about_view, name='about'),
]
```

#### Update `auth_project/urls.py`

Include the blog app's URLs and Django's built-in authentication URLs.

```python
# auth_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include Django's built-in auth URLs (for /accounts/login/, /accounts/logout/, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    # Include our blog app's URLs
    path('', include('blog.urls')),
]
```

---

### Step 6: Create Templates

Create the necessary HTML templates in `blog/templates/blog/`.

1.  **Create the directory structure:**
    ```bash
    mkdir -p blog/templates/blog
    ```

2.  **`blog/templates/blog/base.html` (Base template for consistent layout)**

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Django Auth Blog - {% block title %}{% endblock %}</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            nav { margin-bottom: 20px; }
            nav a { margin-right: 15px; text-decoration: none; color: #007bff; }
            nav a:hover { text-decoration: underline; }
            .container { max-width: 800px; margin: auto; }
            .post { border: 1px solid #ddd; padding: 15px; margin-bottom: 10px; border-radius: 5px; }
            .post h2 { margin-top: 0; }
            .actions a { margin-right: 10px; }
            .errorlist { color: red; }
            .message { background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb; padding: 10px; border-radius: 5px; margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <div class="container">
            <nav>
                <a href="{% url 'post_list' %}">Home</a>
                <a href="{% url 'post_create' %}">New Post</a>
                <a href="{% url 'about' %}">About</a>
                {% if user.is_authenticated %}
                    <span>Welcome, {{ user.username }}!</span>
                    <a href="{% url 'logout' %}">Logout</a>
                {% else %}
                    <a href="{% url 'login' %}">Login</a>
                {% endif %}
            </nav>
            <hr>
            {% if messages %}
                <ul class="messages">
                    {% for message in messages %}
                    <li{% if message.tags %} class="{{ message.tags }}"{% endif %}>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}
            <h1>{% block page_title %}{% endblock %}</h1>
            {% block content %}
            {% endblock %}
        </div>
    </body>
    </html>
    ```

3.  **`blog/templates/blog/post_list.html`**

    ```html
    {% extends 'blog/base.html' %}

    {% block title %}Post List{% endblock %}

    {% block page_title %}Blog Posts{% endblock %}

    {% block content %}
        {% for post in posts %}
            <div class="post">
                <h2><a href="{% url 'post_detail' post.pk %}">{{ post.title }}</a></h2>
                <p>by {{ post.author.username }} on {{ post.created_at|date:"M d, Y" }}</p>
                <div class="actions">
                    {# Authorization checks for display purposes #}
                    {% if user == post.author or user.groups.filter(name='Editor').exists %}
                        <a href="{% url 'post_update' post.pk %}">Edit</a>
                    {% endif %}
                    {% if user.is_superuser %}
                        <a href="{% url 'post_delete' post.pk %}" style="color:red;">Delete</a>
                    {% endif %}
                </div>
            </div>
        {% empty %}
            <p>No posts yet. <a href="{% url 'post_create' %}">Be the first to create one!</a></p>
        {% endfor %}
    {% endblock %}
    ```

4.  **`blog/templates/blog/post_detail.html`**

    ```html
    {% extends 'blog/base.html' %}

    {% block title %}{{ post.title }}{% endblock %}

    {% block page_title %}{{ post.title }}{% endblock %}

    {% block content %}
        <p>by {{ post.author.username }} on {{ post.created_at|date:"M d, Y" }}</p>
        <p>{{ post.content }}</p>
        <div class="actions">
            {% if user == post.author or user.groups.filter(name='Editor').exists %}
                <a href="{% url 'post_update' post.pk %}">Edit Post</a>
            {% endif %}
            {% if user.is_superuser %}
                <a href="{% url 'post_delete' post.pk %}" style="color:red;">Delete Post</a>
            {% endif %}
        </div>
        <p><a href="{% url 'post_list' %}">Back to all posts</a></p>
    {% endblock %}
    ```

5.  **`blog/templates/blog/post_form.html` (for Create and Update)**

    ```html
    {% extends 'blog/base.html' %}

    {% block title %}{{ page_title }}{% endblock %}

    {% block page_title %}{{ page_title }}{% endblock %}

    {% block content %}
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Save Post</button>
        </form>
        <p><a href="{% url 'post_list' %}">Cancel</a></p>
    {% endblock %}
    ```

6.  **`blog/templates/blog/post_confirm_delete.html`**

    ```html
    {% extends 'blog/base.html' %}

    {% block title %}{{ page_title }}{% endblock %}

    {% block page_title %}{{ page_title }}{% endblock %}

    {% block content %}
        <p>Are you sure you want to delete the post "{{ post.title }}"?</p>
        <form method="post">
            {% csrf_token %}
            <button type="submit">Confirm Delete</button>
        </form>
        <p><a href="{% url 'post_list' %}">Cancel</a></p>
    {% endblock %}
    ```

7.  **`blog/templates/blog/about.html` (for public page)**

    ```html
    {% extends 'blog/base.html' %}

    {% block title %}About Us{% endblock %}

    {% block page_title %}About Our Blog{% endblock %}

    {% block content %}
        <p>This is a simple blog application built to demonstrate Django's authentication and authorization features, along with system design principles.</p>
        <p>Enjoy learning!</p>
    {% endblock %}
    ```

8.  **Login and Logout Templates (provided by Django auth app)**
    Django's `django.contrib.auth.urls` expects specific templates for login and logout. You can override them, but for this practical, we'll ensure they exist. Create `templates/registration/login.html` and `templates/registration/logged_out.html` in your *project root* (not inside `blog/templates/blog`).

    ```bash
    mkdir -p templates/registration
    ```

    **`templates/registration/login.html`**

    ```html
    {% extends 'blog/base.html' %}

    {% block title %}Login{% endblock %}

    {% block page_title %}Login{% endblock %}

    {% block content %}
        {% if form.errors %}
            <p>Your username and password didn't match. Please try again.</p>
        {% endif %}

        {% if next %}
            {% if user.is_authenticated %}
                <p>Your account doesn't have access to this page. To proceed,
                please login with an account that has access.</p>
            {% else %}
                <p>Please login to see this page.</p>
            {% endif %}
        {% endif %}

        <form method="post" action="{% url 'login' %}">
            {% csrf_token %}
            <p>
                <label for="{{ form.username.id_for_label }}">Username:</label>
                {{ form.username }}
            </p>
            <p>
                <label for="{{ form.password.id_for_label }}">Password:</label>
                {{ form.password }}
            </p>
            <input type="submit" value="Login">
            <input type="hidden" name="next" value="{{ next }}">
        </form>
        <p><a href="{% url 'post_list' %}">Back to home</a></p>
    {% endblock %}
    ```

    **`templates/registration/logged_out.html`**

    ```html
    {% extends 'blog/base.html' %}

    {% block title %}Logged Out{% endblock %}

    {% block page_title %}Logged Out{% endblock %}

    {% block content %}
        <p>You have been successfully logged out.</p>
        <p><a href="{% url 'login' %}">Log in again</a></p>
    {% endblock %}
    ```

---

### Step 7: Global Access Control Middleware

Now, let's implement the middleware to redirect unauthenticated users from most of the site.

1.  **Create `blog/middleware.py`:**

    ```python
    # blog/middleware.py
    from django.shortcuts import redirect
    from django.urls import reverse, resolve, Resolver404
    from django.conf import settings

    class LoginRequiredMiddleware:
        def __init__(self, get_response):
            self.get_response = get_response
            self.login_url = settings.LOGIN_URL # '/accounts/login/'
            self.admin_url_prefix = '/admin/'

            # List of URL names that should be publicly accessible
            # We explicitly allow 'login', 'logout', and 'about'
            self.public_url_names = ['login', 'logout', 'about'] 

        def __call__(self, request):
            # --- Check for public paths ---
            is_public_path = False
            # Check if it's the login URL itself or an admin path
            if request.path == self.login_url or request.path.startswith(self.admin_url_prefix):
                is_public_path = True
            else:
                # Try to resolve the URL name to check against public_url_names
                try:
                    resolver_match = resolve(request.path_info)
                    if resolver_match.url_name in self.public_url_names:
                        is_public_path = True
                except Resolver404:
                    # If URL doesn't resolve to a named view, it's not in our public_url_names
                    pass # Keep is_public_path as False

            # --- Enforce login for non-public paths ---
            if not request.user.is_authenticated and not is_public_path:
                # Redirect to login page, preserving the original requested path
                # so the user can be redirected back after successful login.
                return redirect(f"{self.login_url}?next={request.path}")

            # If authenticated, or if it's a public path, proceed to the next middleware/view
            response = self.get_response(request)
            return response
    ```

2.  **Register the Middleware in `auth_project/settings.py`:**
    Add your custom middleware after `AuthenticationMiddleware`.

    ```python
    # auth_project/settings.py
    MIDDLEWARE = [
        # ... (default Django middleware)
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware', # Place our middleware AFTER this
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        # Our custom middleware for global login enforcement
        'blog.middleware.LoginRequiredMiddleware', 
    ]
    ```

---

### Step 8: Test Your Application

Now everything is set up! Run your server and test the authorization logic.

```bash
python manage.py runserver
```

Open your browser to `http://127.0.0.1:8000/`.

**Test Scenarios:**

1.  **Guest User:**
    *   Try to access `http://127.0.0.1:8000/`. You should be immediately redirected to `/accounts/login/`.
    *   Try to access `http://127.0.0.1:8000/about/`. You should be able to see the "About Us" page without logging in (because it's marked as public in our middleware).
2.  **Normal User (e.g., `user`):**
    *   Log in as `user` (password `password123`).
    *   Create a new post.
    *   Try to edit your *own* post. It should work.
    *   Create a second post, then log out and log in as `editor`.
    *   Log back in as `user`. Try to edit the post created by `editor`. You should receive a "You do not have permission to edit this post." (HTTP 403) error.
    *   Try to delete any post. You should receive a "You do not have permission to edit this post." (HTTP 403) error because the `PostDeleteView` requires superuser status.
3.  **Editor User (e.g., `editor`):**
    *   Log in as `editor` (password `password123`).
    *   Try to edit a post created by `user`. It should work (due to group membership).
    *   Try to delete any post. You should receive a "You do not have permission to edit this post." (HTTP 403) error.
4.  **Admin User (e.g., `admin`):**
    *   Log in as `admin` (password `password123`).
    *   Create, edit, and view any post.
    *   Try to delete any post. It should work.

---

### Conclusion to Module 1

Congratulations! You've successfully built a basic Django blog application with robust authentication and granular authorization. You've implemented:
*   User accounts and basic login/logout.
*   Protection of views using `@login_required` and `LoginRequiredMixin`.
*   Object-level authorization to allow authors to edit their own content.
*   Role-based access control using Django Groups for "Editor" functionality.
*   Superuser-only access for sensitive actions like deleting posts.
*   A global middleware to enforce site-wide login requirements.

This project serves as a strong foundation for understanding how security and access control are fundamental aspects of system design. In Module 2, we'll abstract away from the code slightly and discuss broader architectural patterns.