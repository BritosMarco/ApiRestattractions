from rest_framework.viewsets import ModelViewSet
from localization.models import Address
from .serializers import LocalizationsSerializer


class LocalizationsViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = LocalizationsSerializer
