Perfect 👍
Let’s **build a complete mini Django authorization project** step-by-step.
This is **hands-on**, **simple**, and **real-world**.

You can literally type along.

---

# 🧱 Mini Django Authorization Project

### **What we are building**

A **Blog app** with:

* Users can **log in**
* Users can **create posts**
* Users can **edit only their own posts**
* **Editors** can edit any post
* **Admins** can delete posts
* Middleware enforces **global rules**

---

## 🛠️ Tech Stack

* Django (no DRF yet)
* Django auth (User, Groups, Permissions)
* Custom middleware

---

## 📁 Project Structure

```
auth_project/
│
├── auth_project/
│   ├── settings.py
│   ├── urls.py
│
├── blog/
│   ├── models.py
│   ├── views.py
│   ├── middleware.py
│   ├── urls.py
│
├── templates/
│
└── manage.py
```

---

## 🚀 Step 1: Create Project & App

```bash
django-admin startproject auth_project
cd auth_project
python manage.py startapp blog
```

Add app to `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'blog',
    'django.contrib.auth',
]
```

---

## 🧩 Step 2: Blog Model

`blog/models.py`

```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 🔐 Step 3: Create Users & Groups

```bash
python manage.py createsuperuser
```

Then open admin:

```
/admin
```

### Create Groups

* **Editor**

  * `change_post`
  * `view_post`
* **Admin**

  * all permissions

Assign users to groups.

---

## 👀 Step 4: Views with Authorization Logic

`blog/views.py`

```python
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import Post

@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Authorization rule
    if post.author != request.user and not request.user.groups.filter(name='Editor').exists():
        return HttpResponseForbidden("You cannot edit this post")

    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.save()
        return redirect('posts')

    return render(request, 'edit.html', {'post': post})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if not request.user.is_superuser:
        return HttpResponseForbidden("Admins only")

    post.delete()
    return redirect('posts')
```

---

## 🧭 Step 5: URLs

`blog/urls.py`

```python
from django.urls import path
from .views import post_list, edit_post, delete_post

urlpatterns = [
    path('', post_list, name='posts'),
    path('edit/<int:post_id>/', edit_post, name='edit'),
    path('delete/<int:post_id>/', delete_post, name='delete'),
]
```

Main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]
```

---

## 🧱 Step 6: Authorization Middleware

### Global rule:

👉 Only logged-in users can access site (except login & admin)

`blog/middleware.py`

```python
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            not request.user.is_authenticated and
            request.path not in [reverse('login')] and
            not request.path.startswith('/admin/')
        ):
            return redirect('login')

        return self.get_response(request)
```

Register it in `settings.py`:

```python
MIDDLEWARE = [
    ...
    'blog.middleware.LoginRequiredMiddleware',
]
```

---

## 🔑 Step 7: Login Setup

Add this to `settings.py`:

```python
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
```

Add auth URLs:

```python
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
```

Login page:

```
/accounts/login/
```

---

## 🧠 Step 8: Authorization Rules (Summary)

| Action      | Rule                |
| ----------- | ------------------- |
| View posts  | Logged in           |
| Edit post   | Owner OR Editor     |
| Delete post | Admin only          |
| Access site | Middleware-enforced |

---

## 🧪 Step 9: Test Scenarios

1. Normal user:

   * Can edit **own post**
   * ❌ Cannot edit others
2. Editor:

   * Can edit **any post**
3. Admin:

   * Can delete posts
4. Guest:

   * Redirected to login

---

## ✅ What You Just Learned

✔ Django permissions
✔ Groups & roles
✔ Object-level authorization
✔ Middleware authorization
✔ Real production patterns

---

## 🔥 Next Level (Optional)
