from operator import mod
from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.TextField()
    description = models.TextField()