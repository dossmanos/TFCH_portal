from rest_framework.serializers import ModelSerializer
from base.models import Concert

class ConcertSerializer(ModelSerializer):
    class Meta:
        model = Concert
        fields = '__all__'
