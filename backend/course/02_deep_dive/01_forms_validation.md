# Lesson 1: Working with Forms & Data Validation

Most web applications need to accept user input. Django's **Form** system handles everything from generating the HTML forms to validating the data and handling errors.

---

### 1. Why Use Django Forms?
*   **Automatic Generation:** Django can generate HTML form fields based on your models or custom requirements.
*   **Validation:** It automatically ensures the data is in the correct format (e.g., valid email, required fields).
*   **Security:** It includes built-in CSRF protection to prevent common web attacks.

### 2. Creating a ModelForm
The fastest way to create a form for a model is to use a `ModelForm`.

In `blog/forms.py`:
```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content'] # Fields to include in the form
```

### 3. Using the Form in a View
In `blog/views.py`:
```python
from django.shortcuts import render, redirect
from .forms import PostForm

def create_post_view(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = PostForm(request.POST)
        if form.is_valid():
            # Data is valid, save to database
            form.save()
            return redirect('post_list')
    else:
        # GET request, show an empty form
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})
```

### 4. Displaying the Form in a Template
In `blog/templates/blog/create_post.html`:
```html
<form method="post">
    {% csrf_token %} <!-- Mandatory security token -->
    {{ form.as_p }} <!-- Display form fields as <p> tags -->
    <button type="submit">Create Post</button>
</form>
```

### 5. Custom Validation
You can add custom logic to validate specific fields by adding a `clean_<fieldname>()` method to your form class.

```python
# blog/forms.py
class PostForm(forms.ModelForm):
    # ...
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "Bad Word" in title:
            raise forms.ValidationError("Please choose a better title!")
        return title
```

---
**Summary:**
*   Forms are the bridge between your users and your database.
*   `ModelForm` is perfect for CRUD operations.
*   Always include `{% csrf_token %}` in your forms.
*   Validation happens automatically but can be customized with `clean()` methods.
