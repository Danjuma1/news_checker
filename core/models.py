from django.db import models


class News(models.Model):
    headline = models.CharField(max_length=150)
    content = models.TextField()