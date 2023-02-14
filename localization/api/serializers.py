from rest_framework.serializers import ModelSerializer
from localization.models import Address


class LocalizationsSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
