# Lesson 6: Views, URLs, and Templates: The MVT in Action

This lesson demonstrates how Django's **Model-View-Template (MVT)** pattern works together to display content to a user. We'll create a simple page that lists all our blog posts.

---

### 1. Step 1: Create a View
In `blog/views.py`:
```python
from django.shortcuts import render
from .models import Post

def post_list_view(request):
    # Fetch all post objects from the database
    posts = Post.objects.all()
    # Pass the posts to the template
    return render(request, 'blog/post_list.html', {'posts_list': posts})
```

### 2. Step 2: Create a Template
Django looks for templates in a folder named `templates` within your app directory.

Create `blog/templates/blog/post_list.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
</head>
<body>
    <h1>Latest Posts</h1>
    <ul>
        {% for post in posts_list %}
            <li>
                <strong>{{ post.title }}</strong> - {{ post.created_at }}
                <p>{{ post.content|truncatewords:20 }}</p>
            </li>
        {% empty %}
            <li>No posts yet.</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### 3. Step 3: Configure URL Routing
Routing happens in two stages: project-level and app-level.

**Project-level (`mywebsite/urls.py`):**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # Link to app's URLs
]
```

**App-level (`blog/urls.py`):**
```python
from django.urls import path
from .views import post_list_view

urlpatterns = [
    path('', post_list_view, name='post_list'),
]
```

### 4. Step 4: Access the View
1.  Run the development server: `python manage.py runserver`
2.  Navigate to `http://127.0.0.1:8000/blog/` in your browser.
3.  You should now see the list of posts you created in the admin!

---
**Summary:**
*   **V (View):** Fetches data and handles logic.
*   **T (Template):** Defines how data is displayed using Django's template language.
*   **URLs:** Map requests to the correct view.
*   Always use app-level `urls.py` for cleaner project organization.
