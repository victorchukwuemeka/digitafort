# Hands-On Guide: Build a Mini Django Authorization Project

This is a practical, step-by-step tutorial for building a simple but realistic Django blog application with a robust authorization system.

---

### **Project Goal**

We will build a blog where:
*   Users can log in and view posts.
*   Users can create posts.
*   Users can **only edit their own** posts.
*   A special **"Editor" group** can edit **any** post.
*   Only **"Admins" (superusers)** can delete posts.
*   A middleware will block any non-logged-in user from accessing the site.

---

### **Prerequisites**

*   Python and `pip` installed on your system.
*   Basic knowledge of Python and the command line.
*   Virtual environment (recommended): `python -m venv venv` and `source venv/bin/activate` (or `venv\Scripts\activate` on Windows).

---

## **🚀 Step 1: Project Setup**

First, let's get the Django project and our `blog` app running.

```bash
# Install Django
pip install Django

# Create the project and navigate into it
django-admin startproject auth_project
cd auth_project

# Create the blog app
python manage.py startapp blog
```

Now, register the `blog` app in `auth_project/settings.py`.

```python
# auth_project/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Register our new app
    'blog',
]
```

---

## **🧩 Step 2: The `Post` Model**

Define the model for our blog posts in `blog/models.py`. This sets up the database structure.

```python
# blog/models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Link each post to a user (the author)
    # If an author is deleted, all their posts are also deleted.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
```

Now, apply this model to your database.
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## **🔐 Step 3: Create Users and Groups**

Authorization is all about users and their roles.

**1. Create a Superuser (Admin):**
This user will have all permissions.
```bash
python manage.py createsuperuser
# Follow the prompts to create your admin user.
```

**2. Create an "Editor" Group:**
*   Run your server: `python manage.py runserver`
*   Navigate to the admin panel: `http://127.0.0.1:8000/admin/`
*   Log in with your superuser account.
*   Go to "Groups" -> "Add Group".
*   Name the group `Editor`.
*   In the permissions box, find `blog | post` and assign it `Can change post` and `Can view post`. Save the group.

**3. Create Normal Users:**
*   In the admin panel, go to "Users" -> "Add User".
*   Create a "normaluser" and a user you'll make an editor, "editoruser".
*   Assign "editoruser" to the `Editor` group.

---

## **👀 Step 4: The Views (Where the Logic Lives)**

Here in `blog/views.py`, we'll implement the core authorization logic.

```python
# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Post

# Every view from here on requires the user to be logged in.
@login_required
def post_list(request):
    posts = Post.objects.all()
    # Render a page showing all posts.
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # The core authorization check:
    # Is the current user the author? OR is the user in the 'Editor' group?
    is_author = post.author == request.user
    is_editor = request.user.groups.filter(name='Editor').exists()

    if not (is_author or is_editor):
        # If they are neither, they are forbidden from editing.
        return HttpResponseForbidden("You do not have permission to edit this post.")

    if request.method == 'POST':
        # Handle the form submission
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('post_list') # Redirect back to the list of posts

    # If it's a GET request, show the edit form.
    return render(request, 'blog/edit_post.html', {'post': post})

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Only a superuser can delete posts.
    if not request.user.is_superuser:
        return HttpResponseForbidden("Only administrators can delete posts.")

    post.delete()
    return redirect('post_list')
```

---

## **📄 Step 5: The Templates (The User Interface)**

Create a `templates/blog` directory. Django will automatically find templates here.

**`templates/blog/post_list.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>All Posts</title>
</head>
<body>
    <h1>Posts</h1>
    <p>Welcome, {{ request.user.username }}! <a href="{% url 'logout' %}">Logout</a></p>
    <ul>
        {% for post in posts %}
            <li>
                <strong>{{ post.title }}</strong> by {{ post.author.username }}
                <a href="{% url 'edit_post' post.id %}">Edit</a> | 
                <a href="{% url 'delete_post' post.id %}" style="color:red;">Delete</a>
            </li>
        {% empty %}
            <li>No posts yet.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

**`templates/blog/edit_post.html`**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Edit Post</title>
</head>
<body>
    <h1>Edit Post</h1>
    <form method="post">
        {% csrf_token %}
        <input type="text" name="title" value="{{ post.title }}" required>
        <br><br>
        <textarea name="content" rows="10" cols="50" required>{{ post.content }}</textarea>
        <br><br>
        <button type="submit">Save Changes</button>
    </form>
    <a href="{% url 'post_list' %}">Cancel</a>
</body>
</html>
```

---

## **🧭 Step 6: URL Configuration**

Wire up the views, admin, and authentication URLs.

**`blog/urls.py` (Create this file)**
```python
from django.urls import path
from .views import post_list, edit_post, delete_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]
```

**`auth_project/urls.py` (The main URL file)**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the built-in authentication views (for login, logout, etc.)
    path('accounts/', include('django.contrib.auth.urls')),
    # Include our blog app's URLs
    path('', include('blog.urls')),
]
```

---

## **🧱 Step 7: Global Middleware**

Let's add a middleware to ensure only logged-in users can access *any* part of our site, except for the login page itself.

**`blog/middleware.py` (Create this file)**
```python
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = reverse('login')
        self.admin_prefix = '/admin/'

    def __call__(self, request):
        # Check if the user is authenticated and if the path is not already the login page or admin
        if (not request.user.is_authenticated 
            and request.path != self.login_url 
            and not request.path.startswith(self.admin_prefix)):
            return redirect(self.login_url)

        return self.get_response(request)
```

**Register the middleware in `auth_project/settings.py`:**
Place it after `AuthenticationMiddleware`.
```python
MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Add our custom middleware here
    'blog.middleware.LoginRequiredMiddleware',
]
```

**Finally, add login/logout redirect URLs in `settings.py`:**
```python
# auth_project/settings.py
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
```

---

## **🧪 Step 8: Test Your Application**

Run `python manage.py runserver` and try these scenarios:
1.  **Go to `http://127.0.0.1:8000/` as a guest.** You should be redirected to the login page (`/accounts/login/`).
2.  **Log in as the "normaluser".** You should be able to edit your own posts but get a "Forbidden" error if you try to edit another user's post or delete any post.
3.  **Log in as the "editoruser".** You should be able to edit *any* post but not delete them.
4.  **Log in as the superuser.** You can do everything.

---

## **🔥 What's Next?**

Congratulations! You've built a solid authorization system. To take it to the next level, consider:
*   **Django-Guardian:** For more complex object-level permissions.
*   **Custom User Model:** To add fields like `profile_picture` or `subscription_level` to your users.
*   **Django REST Framework:** Apply the same authorization principles to a web API.
*   **Frontend Integration:** Connect this backend to a React or Vue.js frontend application.