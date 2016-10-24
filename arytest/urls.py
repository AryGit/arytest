from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    url(r'^admin/', include(admin.site.urls)),
    #Sessions
    url(r'^accounts/', include('allauth.urls')),
    #il8n
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^', include('common.urls')),                  
)
