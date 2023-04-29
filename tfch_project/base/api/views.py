from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Concert
from .serializers import ConcertSerializer

@api_view(['GET']) # choosing allowed method
def getRoutes(request):
    get_routes = [
        'GET /api',
        'GET /api/concerts',
        'GET or POST /api/concerts/:id',
    ]
    return Response(get_routes)

@api_view(['GET'])
def getConcerts(request):
    concerts = Concert.objects.all()
    serialized_concerts_list = ConcertSerializer(concerts, many=True)
    return Response(serialized_concerts_list.data)

@api_view(['GET', 'POST'])
def getConcert(request,primary_key):
    concert= Concert.objects.get(id=primary_key)
    if request.method == 'GET':
        serialized_concert = ConcertSerializer(concert, many=False)
        return Response(serialized_concert.data)
    if request.method == 'POST':
        pass