from rest_framework.serializers import ModelSerializer
from commentreviews.models import Comment


class CommentreviewsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
