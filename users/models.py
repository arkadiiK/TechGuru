from django.db import models
from django import forms


class User(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
