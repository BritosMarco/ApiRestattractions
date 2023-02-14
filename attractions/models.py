from django.db import models


class Attractions(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    opening_hours = models.CharField(max_length=150)
    minimun_age = models.IntegerField()

    def __str__(self):
        return self.name
