#encoding:utf-8
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.template import RequestContext
from django.template.loader import render_to_string
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.core.validators import validate_email
from django.db.models import Count, Avg, Sum
from django.utils.html import escape
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.http import HttpResponse
import datetime
from django.db.models import Count, Avg, Sum
from django import forms

from .forms import TareasForm, PerfilForm
from .models import Tarea, Perfil

# Create your views here.
	    
def addUsuario(request):
	if request.method == 'POST':
		perfil_form = PerfilForm(request.POST)
		
		if perfil_form.is_valid():
			perfil_form.save()
			return render_to_response('common/otro.html', {'mensaje': 'Formulario guardado correctamente'}, context_instance=RequestContext(request))
		else:
			return render_to_response('common/otro.html', locals(), context_instance=RequestContext(request))
	else:
		perfil_form = PerfilForm()

		
	return render_to_response('common/otro.html', locals(), context_instance=RequestContext(request))

@login_required
def addTarea(request):
	form = TareasForm()
	if request.method == 'POST':
		form = TareasForm(request.POST)
        if form.is_valid():
		    tarea = form.save(commit=False)
		    tarea.user = request.user
		    tarea.save()
		    return HttpResponseRedirect('/')					
	return render_to_response('common/add_tarea.html',{'form' : form}, context_instance=RequestContext(request))

@login_required
def editTarea(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    mensaje = None
    formTarea = TareasForm(instance=tarea)
    if request.method == 'POST':
		if tarea.realizada == False:
			formTarea = TareasForm(request.POST, instance=tarea)
			if formTarea.is_valid():
				formTarea.save()				
				mensaje = "Tarea modificada con éxito"				
				
		else:
			mensaje = "No se puede editar una tarea marcada como realizada"
			print mensaje
		
    return render_to_response('common/edit_tarea.html', {'formTarea': formTarea, 'id': id, 'mensaje': mensaje }, context_instance=RequestContext(request))

@login_required
def deleteTarea(request, pk):
	mensaje = ""
	fecha_actual = timezone.now()
	
	td = get_object_or_404(Tarea, pk=pk)
	if (td.fecha_registro_tarea < fecha_actual):
		td.delete()
	else:
		mensaje = "La tarea no es considerada como antigua, no puede ser eliminada"
	
	return render_to_response("common/delete_tarea.html", {'mensaje': mensaje}, context_instance=RequestContext(request))

