from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add your custom fields here
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    is_premium_member = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=200, default="Untitled")
    author = models.CharField(max_length=100, default="Unknown Author")
    publication_year = models.IntegerField(default=2000)

    def __str__(self):
        return self.title