# Lesson 1: Automated Testing in Django

Testing is what separates amateur code from professional software. It ensures your application works as expected and helps you catch bugs early before they reach production.

---

### 1. Why Test Your Code?
*   **Confidence:** You can make changes to your codebase without fear of breaking existing features.
*   **Documentation:** Tests act as a form of living documentation for how your code should behave.
*   **Time-Saving:** Catching a bug in development is much faster and cheaper than catching it in production.

### 2. Django's Built-in Testing Framework
Django's testing framework is based on Python's `unittest` library but includes many useful additions for web development.

To run your tests:
```bash
python manage.py test
```

### 3. Writing a Simple Unit Test
Unit tests check the behavior of small, isolated parts of your code (e.g., a single model method).

In `blog/tests.py`:
```python
from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def test_string_representation(self):
        post = Post.objects.create(title="My Post", content="Hello!")
        self.assertEqual(str(post), "My Post")
```

### 4. Writing an Integration Test
Integration tests check how different parts of your application work together (e.g., a view interacting with a model).

```python
from django.urls import reverse

class PostViewTest(TestCase):
    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
```

### 5. Mocking External Dependencies
Sometimes your code depends on external services (like an email API). You should **Mock** these dependencies to keep your tests fast and reliable.

```python
from unittest.mock import patch

class EmailTest(TestCase):
    @patch('my_app.services.send_email')
    def test_email_sent(self, mock_send):
        # ... call code that sends email ...
        self.assertTrue(mock_send.called)
```

---
**Summary:**
*   Always write tests for your core business logic.
*   Run `python manage.py test` frequently.
*   Aim for a mix of small Unit tests and larger Integration tests.
*   Mock external services to avoid slow or unreliable tests.
