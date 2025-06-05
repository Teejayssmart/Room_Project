from django.urls  import path, include
from room_listing.api.views import room_list, room_detail

urlpatterns = [
    path('list/',room_list, name='room-list'),
    path('<int:pk>/',room_detail, name='room-detail'),
]
