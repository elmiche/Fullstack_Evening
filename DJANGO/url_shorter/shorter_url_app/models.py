from django.db import models
from django.utils import timezone
# Create your models here.git

class Shorter_url(models.Model):
    url = models.URLField()
    shorty = models.CharField(max_length = 5, default='', editable=False)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.shorty
        #cleans up the admin panel