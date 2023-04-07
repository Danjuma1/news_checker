from django.db import models
from django.contrib.auth.models import User


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="Unkown", blank=True)
    content = models.TextField()
    label = models.CharField(max_length=10)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.headline