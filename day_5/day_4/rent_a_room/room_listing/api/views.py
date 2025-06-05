from rest_framework.response import Response
from rest_framework.decorators import api_view
from room_listing.models import Room
from room_listing.api.serializers import RoomSerializer

@api_view(['GET', 'POST'])
def room_list(request):
  #check if request is GET and do this: 
  if request.method == 'GET':
      rooms = Room.objects.all()
      serializer = RoomSerializer(rooms, many=True)
      return Response(serializer.data)
  
  if request.method == 'POST':
    #To get data from User,create serializer
     serializer = RoomSerializer(data=request.data)
     if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
     else:
       return Response(serializer.errors)
    
 
@api_view(['GET', 'PUT', 'DELETE'])
def room_detail(request, pk):
  if request.method == 'GET':
      room = Room.objects.get(pk=pk)
      serializer = RoomSerializer(room)
      return Response(serializer.data)
    
  if request.method == 'PUT':
     room = Room.objects.get(pk=pk)
      #To get data from User,create serializer
     serializer = RoomSerializer(data=request.data)
     if serializer.is_valid():
       serializer.save()
       return Response(serializer.data)
     else:
       return Response(serializer.errors)
    
    
  if request.method == 'DELETE':  
    room = Room.objects.get(pk=pk)
    room.delete()
    return Response()
      
      