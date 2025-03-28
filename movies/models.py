from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title