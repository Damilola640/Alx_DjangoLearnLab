from django.db import models
from django.utils import timezone

# Book model: Represents a book linked to an Author
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        
        related_name="book",  # Enables Author.book to access related books
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

# Author model: Represents an author who can write multiple books
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
