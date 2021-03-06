from django.db import models
from django.utils import timezone


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    author = models.CharField(max_length=10)
    time = models.DateTimeField(default=timezone.now)
