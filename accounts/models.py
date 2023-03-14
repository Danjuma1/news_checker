from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age_range = models.CharField(max_length=50, default="Choose One")
    
    def __str__(self):
        return self.user.username + " - " + self.age_range