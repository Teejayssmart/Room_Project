from rest_framework import status
from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from room_listing.models import Room_watch_list, Room_types
from room_listing.api.serializers import Room_watch_listSerializer, Room_typesSerializer

class Room_typesAV(APIView):
  
    def get(self, request):
      types = Room_types.objects.all()
      serializer = Room_typesSerializer(types, many=True)
      return Response(serializer.data)
    
    def post(self, request):
      serializer = Room_typesSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      else:
        return Response(serializer.errors)
      
    
#this is how to write class based api views
class Room_watch_listAV(APIView):
    def get(self, request):
      rooms = Room_watch_list.objects.all()# gets all records from database
      serializer = Room_watch_listSerializer(rooms, many=True)#converts data into JSON
      return Response(serializer.data)
   
    def post(self, request):
        serializer = Room_watch_listSerializer(data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        else:
          return Response(serializer.errors)
     
   
   
class Room_watch_list_DetailAV(APIView):
   def get(self, request,pk):
     try:
        room = Room_watch_list.objects.get(pk=pk)
     except Room_watch_list.DoesNotExist:
        return Response({'error': 'not found'}, status=status.HTTP_404_NOT_FOUND)
      
     serializer = Room_watch_listSerializer(room)
     return Response(serializer.data)
   
   def put(self, request,pk):  
      room = Room_watch_list.objects.get(pk=pk)
      serializer = Room_watch_listSerializer(room, data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
   def delete(self, request,pk): 
     room = Room_watch_list.objects.get(pk=pk)
     room.delete()
     return Response(status=status.HTTP_204_NO_CONTENT) 
        
  
  
   
   
   
# @api_view(['GET', 'POST'])
# def room_list(request):
#   #check if request is GET and do this: 
#   if request.method == 'GET':
#       rooms = Room.objects.all()
#       serializer = RoomSerializer(rooms, many=True)
#       return Response(serializer.data)
  
#   if request.method == 'POST':
#     #To get data from User,create serializer
#      serializer = RoomSerializer(data=request.data)
#      if serializer.is_valid():
#        serializer.save()
#        return Response(serializer.data)
#      else:
#        return Response(serializer.errors)
    
 
# @api_view(['GET', 'PUT', 'DELETE'])
# def room_detail(request, pk):
#   if request.method == 'GET':
      
  #     try:
  #       room = Room.objects.get(pk=pk)
  #     except Room.DoesNotExist:
  #       return Response({'error:' 'Room not found'}, status=status.HTTP_404_NOT_FOUND)
      
  #     serializer = RoomSerializer(room)
  #     return Response(serializer.data)
    
  # if request.method == 'PUT':
  #    room = Room.objects.get(pk=pk)
  #     #To get data from User,create serializer
  #    serializer = RoomSerializer(data=request.data)
  #    if serializer.is_valid():
  #      serializer.save()
  #      return Response(serializer.data)
  #    else:
  #      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
  # if request.method == 'DELETE':  
  #   room = Room.objects.get(pk=pk)
  #   room.delete()
  #   return Response(status=status.HTTP_204_NO_CONTENT)
      
      