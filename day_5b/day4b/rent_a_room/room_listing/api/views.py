from rest_framework import status
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
      
      try:
        room = Room.objects.get(pk=pk)
      except Room.DoesNotExist:
        return Response({'error:' 'Room not found'}, status=status.HTTP_404_NOT_FOUND)
      
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
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
  if request.method == 'DELETE':  
    room = Room.objects.get(pk=pk)
    room.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
      
      