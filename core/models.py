from django.db import models


class News(models.Model):
    headline = models.CharField(max_length=200)
    author = models.CharField(max_length=100, default="Unkown", blank=True)
    content = models.TextField()
    label = models.CharField(max_length=10)

    def __str__(self):
        return self.headline