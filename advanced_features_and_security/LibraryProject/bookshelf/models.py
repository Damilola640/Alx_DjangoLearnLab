from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200, default="Untitled")
    author = models.CharField(max_length=100, default="Unknown Author")
    publication_year = models.IntegerField(default=2000)

    def __str__(self):
        return self.title

    # Additional Information (Using AbstractUser).
    class CustomUser(AbstractUser):
        date_of_birth = models.DateField(null=True, blank=True)
        profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

        def __str__(self):
            return self.username
        
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        if not username:
            raise ValueError('The username field must be set')
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email, **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, email, password, **extra_fields)

    
# Permissions
class Permissions(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        permissions = [
            ('can_view', 'Can view contents'),
            ('can_create', 'Can create contents'),
            ('can_edit', 'Can edit contents'),
            ('can_delete', 'Can delete contents'),
        ]
        
    def __str__(self):
        return self.title