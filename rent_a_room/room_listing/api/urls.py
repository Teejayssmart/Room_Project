from django.urls  import path, include
#from room_listing.api.views import room_list, room_detail
from room_listing.api.views import Room_watch_listAV, Room_watch_list_DetailAV, Room_typesAV 

urlpatterns = [
    path('list/',Room_watch_listAV.as_view(), name='room-list'),
    path('<int:pk>/',Room_watch_list_DetailAV.as_view(), name='room-detail'),
    path('types/', Room_typesAV.as_view(), name='room-types'),  # Added new URL pattern for room types
]
