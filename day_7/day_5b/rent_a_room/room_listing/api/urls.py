from django.urls  import path, include
#from room_listing.api.views import room_list, room_detail
from room_listing.api.views import RoomListAV, RoomDetailAV

urlpatterns = [
    path('list/',RoomListAV.as_view(), name='room-list'),
    path('<int:pk>/',RoomDetailAV.as_view(), name='room-detail'),
]
