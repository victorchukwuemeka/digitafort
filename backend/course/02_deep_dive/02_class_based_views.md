# Lesson 2: Class-Based Views (CBVs): The Standard for Django

While **Function-Based Views (FBVs)** are easy to understand, **Class-Based Views (CBVs)** offer more structure, code reusability, and cleaner code for common tasks like listing objects, showing details, and creating/updating records.

---

### 1. Why Use Class-Based Views?
*   **DRY (Don't Repeat Yourself):** Most CRUD operations follow a predictable pattern.
*   **Extensibility:** You can inherit from standard views and only override the parts you need.
*   **Built-in Logic:** They handle much of the logic for you (e.g., fetching objects, rendering templates).

### 2. Common Generic Views

| Generic View | Purpose |
| --- | --- |
| **`ListView`** | Display a list of objects (e.g., all blog posts). |
| **`DetailView`** | Show details for a single object. |
| **`CreateView`** | Display and process a form to create a new object. |
| **`UpdateView`** | Display and process a form to update an existing object. |
| **`DeleteView`** | Display a confirmation page and delete an object. |

### 3. Example: Replacing FBVs with CBVs
In `blog/views.py`:
```python
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Instead of a function, use a class
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html' # Default is <app_label>/<model_name>_list.html
    context_object_name = 'posts'         # Default is 'object_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/blog/' # Redirect URL after success
```

### 4. Customizing Your CBVs
You can override methods to add custom behavior:

```python
class PostListView(ListView):
    model = Post
    
    # Custom queryset: only show posts from the last 30 days
    def get_queryset(self):
        return Post.objects.filter(is_published=True).order_by('-created_at')

    # Add extra context to the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Latest News"
        return context
```

### 5. URL Routing with CBVs
When using a class in `urls.py`, you must call `.as_view()`:

```python
# blog/urls.py
from django.urls import path
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'), # CBVs expect 'pk'
]
```

---
**Summary:**
*   CBVs are powerful and standard for large-scale Django projects.
*   Generic views handle repetitive tasks for you.
*   Always call `.as_view()` in `urls.py`.
