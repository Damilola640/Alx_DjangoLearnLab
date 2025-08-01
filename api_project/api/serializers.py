from restframework import serializers
from .models import Book

class BookSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['__all__']  # Include all fields from the Book model
