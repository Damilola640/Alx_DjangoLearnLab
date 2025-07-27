from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, default="Untitled")
    author = models.CharField(max_length=100, default="Unknown Author")
    publication_year = models.IntegerField(default=2000)

    def __str__(self):
        return self.title