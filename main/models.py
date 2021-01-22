from django.db import models

# Create your models here.


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class books(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.CharField(max_length=5)
    genre = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    date = models.DateField(auto_now_add=True)
    is_favorite = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)

    