from django.db import models

class UserLink(models.Model):
    url = models.URLField()
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.url
