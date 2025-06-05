from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    available_from = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.title
