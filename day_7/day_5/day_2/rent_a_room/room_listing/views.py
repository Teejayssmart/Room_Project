from django.shortcuts import render
from room_listing.models import Room
from django.http import JsonResponse

# Create your views here.
def room_list(request):
  rooms = Room.objects.all()
  data = { 'rooms' :list(rooms.values())
          
          }
  return JsonResponse(data)

 # to access each object data 
def room_details(request, pk):
# room = Room.objects.get(pk=pk) is a Django ORM (Object-Relational Mapping) query that means:
# Look into the database table for the Room model
# Find the single Room record where the primary key (pk) equals the value pk (which is passed to the function)
# Return that one Room object as a Python instance and assign it to the variable room
        room = Room.objects.get(pk=pk)
        data = {
                'title' : room.title,
                'description' : room.description,
                'price' : room.price,
                'location' : room.location,
                'available_from' : room.available_from,
                #'owner' : room.owner
                
                 }  
        
        return JsonResponse(data)
        
        