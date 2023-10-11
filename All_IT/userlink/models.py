from django.db import models

class UserLink(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.url

class LinkForIT(models.Model):
    year = models.PositiveIntegerField()
    major = models.CharField(max_length=100)
    link = models.URLField()
    link_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.year} - {self.major}"