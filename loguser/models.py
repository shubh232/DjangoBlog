from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    Description = models.CharField(max_length=10000)
    Author = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)


