from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# from django.contrib.auth.models import get_user_model

class Street_biter(models.Model):
    date_posted =models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=7, decimal_places=7)
    longitude = models.DecimalField(max_digits=7, decimal_places=7) 
    details = models.CharField(max_length=900)
    species = models.CharField(max_length=20)
    # user = models.ForeignKey(get_user_model, on_delete=models.CASCADE)

# class Markers(models.Model):
#     location:
#     date_created:
#     User:
#     coordinates: PointField

#     x:
#     y: