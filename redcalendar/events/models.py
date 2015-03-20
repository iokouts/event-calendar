#import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
#from django.utils import timezone

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateTimeField('date')
    event_place = models.CharField(max_length=100)
    event_poster = models.ImageField(upload_to='posters')

    def __str__(self):
        return self.event_name

   # def __str__(self):
    #    return self.event_place
