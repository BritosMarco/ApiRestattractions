from django.db import models


class Address(models.Model):
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.address1
