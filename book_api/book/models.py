from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    birth_date = models.DateField(null=True, blank=True)
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta():
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(unique=True, max_length=13)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pages = models.IntegerField()
    description = models.TextField(unique=True)
    is_published = models.BooleanField(default=False)
    onwer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    
    


