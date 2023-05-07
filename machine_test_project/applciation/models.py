from datetime import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        # return f"{self.created_at.strftime('%d-%m-%Y')}"


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='projects')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # created_at = models.DateTimeField(default=timezone.now(), editable=True)

    def __str__(self):
        return self.name
