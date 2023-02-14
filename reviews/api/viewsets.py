from rest_framework.viewsets import ModelViewSet
from .serializers import ReviewsSerializers
from reviews.models import ReviewsComment


class ReviewsViewSet(ModelViewSet):
    queryset = ReviewsComment.objects.all()
    serializer_class = ReviewsSerializers
