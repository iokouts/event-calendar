from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['event_name','event_date','event_place','event_poster']
    list_display = ('event_name', 'event_date','event_place')

admin.site.register(Event, EventAdmin)
