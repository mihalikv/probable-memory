from django.db import models

# Create your models here.
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)   

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    readers = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_super_active = models.BooleanField(default=True)
