from django.db import models
from django.utils import timezone
# Create your models here.

class Shorter_url(models.Model):
    content = models.CharField(max_legnth=4000)
    date_posted = models.DateTimeField(models.DateTimeField(default=timezone.now))
    return render()


    def __str__(self):
        return self.title