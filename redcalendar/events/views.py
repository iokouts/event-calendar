from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Event 

from django.utils import timezone
import datetime

def index(request):

    event_list = []

    for e in Event.objects.order_by('from_date'):
        if e.to_date >= timezone.now():
            event_list.append(e)
    
    template = loader.get_template('events/index.html')

    context = RequestContext(request, {'event_list': event_list,})

    return HttpResponse(template.render(context))

def detail(request, event_id):
    return HttpResponse("This is event %s." %event_id)
