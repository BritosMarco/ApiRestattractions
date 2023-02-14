from rest_framework.serializers import ModelSerializer
from reviews.models import ReviewsComment


class ReviewsSerializers(ModelSerializer):
    class Meta:
        model = ReviewsComment
        fields = '__all__'
