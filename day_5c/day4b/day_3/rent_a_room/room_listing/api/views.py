from rest_framework.response import Response
from rest_framework.decorators import api_view
from room_listing.models import Room
from room_listing.api.serializers import RoomSerializer

@api_view()
def room_list(request):
  rooms = Room.objects.all()
  serializer = RoomSerializer(rooms, many=True)
  return Response(serializer.data)
 
@api_view()
def room_detail(request, pk):
  room = Room.objects.get(pk=pk)
  serializer = RoomSerializer(room)
  return Response(serializer.data)
    