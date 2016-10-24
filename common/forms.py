## -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.forms.util import ErrorList
import datetime
from .models import Tarea, Perfil

##------Custom widget para los select------#
class SelectWithPop(forms.Select):
    def render(self, name, *args, **kwargs):
        html = super(SelectWithPop, self).render(name, *args, **kwargs)
        popupplus = render_to_string("form/popupplus.html", {'field': name})
        return html+popupplus
##-----------------------------------------#

##------Custom widget para los select múltiples------#
class SelectWithPopMultiple(forms.SelectMultiple):
    def render(self, name, *args, **kwargs):
        html = super(SelectWithPopMultiple, self).render(name, *args, **kwargs)
        popupplus = render_to_string("form/popupplus.html", {'field': name})
        return html+popupplus
##-----------------------------------------#

class TareasForm(ModelForm):
    class Meta:
        model = Tarea
        exclude = ['user']
    
Lista_Tareas = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=Tarea.objects.all(), required=False)

class PerfilForm(ModelForm):
    class Meta:
        model=Perfil
    
    def clean_email(self):
        data = self.cleaned_data['email']
        if "@gmail.com" not in data:
            raise forms.ValidationError("Invalid email!")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return data


class TareaFormEdit(ModelForm):
	class Meta:
		model = Tarea
