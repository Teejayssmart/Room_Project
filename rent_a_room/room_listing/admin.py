from django.contrib import admin
from room_listing.models import Room_watch_list, Room_types

# Register your models here.
admin.site.register(Room_watch_list)
admin.site.register(Room_types)