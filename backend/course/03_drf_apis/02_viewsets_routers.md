# Lesson 2: API Views, ViewSets & Routers

In DRF, you have several options for creating your API endpoints. This lesson will show you the difference between simple views and the more powerful **ViewSets**.

---

### 1. Simple API Views
You can use `APIView` for fine-grained control, or `generics` (like `ListCreateAPIView`) for standard CRUD operations.

```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListAPIView(generics.ListCreateAPIView):
    # Handles GET (list) and POST (create)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### 2. The Power of ViewSets
A **ViewSet** combines the logic for multiple related views (List, Create, Retrieve, Update, Delete) into a single class.

In `blog/views.py`:
```python
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    # This single class handles all CRUD operations!
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

### 3. Routers: Automating Your URLs
When using ViewSets, you can use a **Router** to automatically generate all your URL patterns.

In `blog/urls.py`:
```python
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='post')

urlpatterns = router.urls
```

### 4. Why Use ViewSets & Routers?
*   **Consistency:** Your URL structure will always be predictable and follow REST conventions.
*   **Speed:** You can create a full-featured CRUD API in just a few lines of code.
*   **Flexibility:** You can still override specific actions (like `list()` or `create()`) if you need custom logic.

---
**Summary:**
*   `APIView` gives you the most control.
*   `Generics` are great for standard patterns.
*   `ViewSets` + `Routers` is the fastest way to build a complete API.
*   Standard REST conventions are your friends.
