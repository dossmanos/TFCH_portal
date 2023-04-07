from rest_framework.serializers import ModelSerializer
from base.models import ChatRoom

class ChatRoomSerializer(ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'
