from django.conf.urls import patterns, include, url
from django.contrib import admin
#from . import views
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^events/', include('events.urls')),

    
    ]
