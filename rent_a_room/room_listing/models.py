from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Room_types(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Room_watch_list(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    available_from = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
