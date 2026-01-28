from email.policy import default

from django.db import models

from datetime import time
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=200)
    floor_number = models.IntegerField()
    room_Number = models.IntegerField()


class Meetings(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default =1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=1)


