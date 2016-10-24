## -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf import settings
from common import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
	#url(r'^$', 'common.views.logueo'),
	#url(r'^inicio/$', 'common.views.logueo'),
	url(r'^$', 'common.views.addTarea', name='add_tarea'),
	url(r'^otro/$', 'common.views.addUsuario', name='add_ususario'),
	url(r'^edit/tarea/(?P<pk>[0-9]+)/$', 'common.views.editTarea', name='edit_tarea'),
	url(r'^delete/tarea/(?P<pk>[0-9]+)/$', 'common.views.deleteTarea', name='delete_tarea'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)





