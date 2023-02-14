from rest_framework.viewsets import ModelViewSet
from commentreviews.models import Comment
from .serializers import CommentreviewsSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentreviewsSerializer


