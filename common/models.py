# -*- coding: utf-8 -*-
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.db.models import Count
from django.db.models.signals import post_save

from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailAddress

## Create your models here.

class Tarea(models.Model):
    user = models.ForeignKey(User)
    nombre = models.CharField("Nombre de la Tarea",max_length=50)
    descripcion = models.TextField("Detalles de la Tarea")
    realizada = models.BooleanField("Realizada", help_text="¿Se encuentra realizada?", default=False)
    fecha_registro_tarea = models.DateTimeField("Fecha en que se registra la tarea", help_text="Formato dia/mes/año Hora:Minutos", null=True, blank=True )
    fecha_realizada_tarea = models.DateTimeField("Fecha en que fue realizada la tarea", help_text="Formato dia/mes/año Hora:Minutos", null=True, blank=True)
    
    def __unicode__(self):
        return  self.nombre + '-' + self.realizada + '-' + self.fecha_registro_tarea+ '-' + self.fecha_realizada_tarea
    
    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"    


class Perfil(models.Model):
    user = models.OneToOneField(User)
    privado = models.BooleanField("Privado", help_text="¿Perfil Privado?", default=False)
    
    class Meta:
        app_label = "auth"
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"

def create_user_profile(sender, instance, created, **kwargs):  
    if created:
       Perfil.objects.create(user=instance)
       if not EmailAddress.objects.filter(email=instance.email):
           address = EmailAddress(user=instance, email=instance.email, verified=True, primary=True)

post_save.connect(create_user_profile, sender=User)
