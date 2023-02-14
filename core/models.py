from django.db import models
from attractions.models import Attractions
from commentreviews.models import Comment
from reviews.models import ReviewsComment
from localization.models import Address


class PontoTuristico(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attractions)
    comment = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(ReviewsComment)
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(
        upload_to='pontos_turisticos', null=True, blank=True)

    def __str__(self):
        return self.name
