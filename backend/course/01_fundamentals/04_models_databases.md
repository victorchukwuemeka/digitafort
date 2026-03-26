# Lesson 4: Models & Databases: The Django ORM

Django's **Object-Relational Mapper (ORM)** is one of its most powerful features. It allows you to interact with your database using Python objects, without writing a single line of SQL.

---

### 1. What is a Model?
A **Model** is a Python class that defines the structure of your data. Each model maps to a single database table, and each attribute of the class maps to a database field.

### 2. Defining a Simple Model
In `blog/models.py`:
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200) # Text field
    content = models.TextField()               # Larger text area
    created_at = models.DateTimeField(auto_now_add=True) # Automatically set when created
```

### 3. Common Field Types
*   **`CharField`:** For short-to-mid-sized strings. Requires `max_length`.
*   **`TextField`:** For long text (e.g., blog content).
*   **`IntegerField`:** For storing integers.
*   **`BooleanField`:** For True/False values.
*   **`DateTimeField`:** For dates and times.
*   **`ForeignKey`:** For defining relationships between models (e.g., a "Post" has an "Author").

### 4. The Migration System: How Django Updates Your DB
When you change your models, you must update the database schema. Django handles this with **Migrations**:

1.  **Generate migration files:**
    ```bash
    python manage.py makemigrations
    ```
2.  **Apply them to the database:**
    ```bash
    python manage.py migrate
    ```

### 5. Interacting with Data (CRUD)
Django provides a simple API for performing **CRUD** (Create, Read, Update, Delete) operations:

*   **Create:** `Post.objects.create(title="Hello", content="World")`
*   **Read (All):** `Post.objects.all()`
*   **Read (Filtered):** `Post.objects.filter(title__contains="Hello")`
*   **Update:** `post.title = "New Title"; post.save()`
*   **Delete:** `post.delete()`

---
**Summary:**
*   Models define your data as Python classes.
*   Migrations keep your database in sync with your models.
*   The Django ORM is your powerful API for interacting with data.
