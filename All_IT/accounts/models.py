from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    sid = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    major = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username