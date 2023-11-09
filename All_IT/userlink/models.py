from django.db import models
from django.contrib.auth.models import User

class UserLink(models.Model):
    link = models.URLField(max_length=255)
    description = models.TextField()
    sid = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Link"

class LinkForIT(models.Model):
    year = models.PositiveIntegerField()
    major = models.CharField(max_length=100)
    link = models.URLField()
    link_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.year} - {self.major}"