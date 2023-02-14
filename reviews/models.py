from django.db import models
from django.contrib.auth.models import User


class ReviewsComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    score = models.DecimalField(max_digits=3, decimal_places=2)
    date_comment = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
