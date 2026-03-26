# Lesson 8: Static & Media Files Management

Websites need to serve more than just HTML. They also need to handle **Static Files** (CSS, JavaScript, images) and **Media Files** (files uploaded by users).

---

### 1. Static vs. Media Files: The Key Difference

*   **Static Files:** These are files that you, the developer, create and ship with your application (e.g., your site's logo, CSS files, and JavaScript code).
*   **Media Files:** These are files that your users upload (e.g., profile pictures, blog post images, or documents).

### 2. Configuring Static Files
In `settings.py`:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] # Where to look for global static files
```

### 3. Using Static Files in Templates
To use a static file, first load the static tag at the top of your template:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

### 4. Configuring Media Files
Unlike static files, media files are NOT part of your source code and need special handling.

In `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media' # Where the actual files are stored
```

In your project's main `urls.py` (to serve media files during development):
```python
from django.conf import settings
from django.conf.urls.static import static

# ... your other urlpatterns ...

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 5. Handling File Uploads in Models
To allow a user to upload a file, use a `FileField` or `ImageField` in your model:

```python
# blog/models.py
class Post(models.Model):
    # ...
    # 'upload_to' defines the subfolder within MEDIA_ROOT
    thumbnail = models.ImageField(upload_to='post_thumbnails/', blank=True, null=True)
```

---
**Summary:**
*   Static files are part of your source code.
*   Media files are uploaded by users.
*   Always use `{% load static %}` and `{% static 'path' %}` in your templates.
*   Special URL configuration is required to serve media files in development.
