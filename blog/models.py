from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title