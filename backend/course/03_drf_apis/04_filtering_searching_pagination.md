# Lesson 4: Filtering, Searching, and Pagination

As your API grows, you'll need ways to manage large sets of data. DRF provides powerful tools for **Filtering**, **Searching**, and **Pagination** right out of the box.

---

### 1. Global Pagination
Pagination splits large lists into smaller, manageable pages.

In `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10 # 10 items per page
}
```

### 2. Basic Filtering
You can filter querysets based on specific fields.

In `blog/views.py`:
```python
class PostViewSet(viewsets.ModelViewSet):
    # ...
    # Simple manual filter
    def get_queryset(self):
        queryset = Post.objects.all()
        author_id = self.request.query_params.get('author_id')
        if author_id:
            queryset = queryset.filter(author_id=author_id)
        return queryset
```

### 3. Advanced Filtering with `django-filter`
For more powerful filtering (e.g., date ranges, numeric ranges), use the `django-filter` library.

```bash
pip install django-filter
```

In `settings.py`:
```python
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}
```

In your view:
```python
class PostViewSet(viewsets.ModelViewSet):
    # ...
    filterset_fields = ['author', 'category'] # Fields you can filter by
```

### 4. Searching & Ordering
DRF's `SearchFilter` and `OrderingFilter` make it easy to add search functionality to your API.

```python
from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    # ...
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content'] # Searchable fields
    ordering_fields = ['created_at', 'title'] # Orderable fields
```

---
**Summary:**
*   Pagination ensures your API stays fast as your database grows.
*   Filtering allows clients to fetch only the data they need.
*   Searching and Ordering are crucial for a great user experience.
*   DRF's built-in filters are powerful and easy to use.
