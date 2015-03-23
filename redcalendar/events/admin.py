from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ['name','from_date','to_date','place','poster']
    list_display = ('name', 'from_date','place')

admin.site.register(Event, EventAdmin)
