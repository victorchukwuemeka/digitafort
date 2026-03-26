# Lesson 1: Introduction to DRF & Serializers

**Django Rest Framework (DRF)** is a powerful and flexible toolkit for building Web APIs. It's the industry standard for building modern, scalable APIs with Django.

---

### 1. What is an API?
An **API (Application Programming Interface)** allows different software systems to communicate with each other. In modern web development, your Django backend will often provide an API for a frontend (like React or Vue) or a mobile app.

### 2. Installing DRF
To start, install DRF and add it to your `INSTALLED_APPS`:
```bash
pip install djangorestframework
```

In `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
]
```

### 3. What is a Serializer?
The **Serializer** is the heart of DRF. It converts complex data types (like Django models) into native Python data types that can then be easily rendered into **JSON**, XML, or other content types. It also handles the reverse: converting incoming JSON back into model objects.

### 4. Creating a Simple Serializer
In `blog/serializers.py`:
```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']
```

### 5. Using Serializers in a View
DRF provides its own set of views for handling API requests.

In `blog/views.py`:
```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

---
**Summary:**
*   DRF is the standard for building APIs in Django.
*   Serializers convert models into JSON and vice-versa.
*   `ModelSerializer` is the fastest way to create a serializer for a Django model.
