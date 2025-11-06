# books/views.py
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Author
from .serializers import BookSerializer, BookDetailSerializer, AuthorSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing authors.
    
    list: Get all authors
    create: Create a new author
    retrieve: Get a specific author
    update: Update an author
    destroy: Delete an author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'bio']
    ordering_fields = ['name', 'created_at']
    ordering = ['name']

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing books.
    """
    queryset = Book.objects.select_related('author', 'owner').all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author', 'is_published']
    search_fields = ['title', 'description', 'author__name']
    ordering_fields = ['title', 'price', 'published_date', 'created_at']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Use detailed serializer for retrieve action"""
        if self.action == 'retrieve':
            return BookDetailSerializer
        return BookSerializer
    
    def perform_create(self, serializer):
        """Set the owner to the current user when creating a book"""
        serializer.save(owner=self.request.user)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def publish(self, request, pk=None):
        """Custom action to publish a book"""
        book = self.get_object()
        book.is_published = True
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def unpublish(self, request, pk=None):
        """Custom action to unpublish a book"""
        book = self.get_object()
        book.is_published = False
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)