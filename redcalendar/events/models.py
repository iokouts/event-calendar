#import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
#from django.utils import timezone

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=200)
    from_date = models.DateTimeField('date')
    to_date = models.DateTimeField('date')
    place = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='posters')

    def __str__(self):
        return self.name

   # def __str__(self):
    #    return self.event_place
