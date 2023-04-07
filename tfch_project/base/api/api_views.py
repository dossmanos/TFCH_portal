from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import ChatRoom
from .serializers import ChatRoomSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET api/',
        'GET api/rooms',
        'GET api/rooms/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = ChatRoom.objects.all()
    serializer = ChatRoomSerializer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request, primary_key):
    room = ChatRoom.objects.get(id=primary_key)
    serializer = ChatRoomSerializer(room, many=False)
    return Response(serializer.data)