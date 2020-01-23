from django.db import models
from django.utils import timezone


class Street_biter(models.Model):
    date_posted =models.DateTimeField(default=timezone.now)
