from django.db import models
from django.utils import timezone
# Create your models here.


class Basic_crud_app(models.Model):
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)


# def __str__(self):
#     return self.message

                            # Do I need this????