from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'name','birth_date','book_count','created_at']
        read_only_fields = ['id', 'created_at']

    def get_book_count(self, obj):
        return obj.books.count()


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    owner_username = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Book
        fields = [
            'id','title','author','author_name','isbn','published_date',
            'price','pages','description','is_published',
            'owner','owner_username'
        ]
        read_only_fields = ['id','owner','created_at','updated_at']

    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero")
        return value
    
    def validate_isbn(self, value):
        if len(value) !=13:
            raise serializers.ValidationError("ISBN must be exaacty 13 cha")
        if not value.isdigit():
            raise serializers.ValidationError("must be digit")
        return value
    
class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Book
        fields = [
            'id', 'title', 'author', 'author_id', 'isbn',
            'published_date', 'price', 'pages', 'description',
            'is_published', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id','created_at','updated_at']

