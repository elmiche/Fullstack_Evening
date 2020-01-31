from django.db import models
from django.utils import timezone


class Street_biter(models.Model):
    date_posted =models.DateTimeField(default=timezone.now)



# class Markers(models.Model):
#     location:
#     date_created:
#     User:
#     coordinates: PointField

#     x:
#     y: