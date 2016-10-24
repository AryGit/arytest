from django.contrib import admin
from django.http import HttpResponse
from django.core import serializers

from .models import Tarea, Perfil

# Register your models here.

def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(mimetype="text/javascript")
    serializers.serialize("json", queryset, stream=response)
    return response

export_as_json.short_description = "Exportar datos seleccionados en un fichero json."

admin.site.add_action(export_as_json, 'export_as_json')


class TareaAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if getattr(obj, 'agregado_por', None) is None:
			obj.agregado_por = request.user
		obj.save()

class PerfilAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if getattr(obj, 'agregado_por', None) is None:
			obj.agregado_por = request.user
		obj.save()


admin.site.register(Tarea,TareaAdmin)
admin.site.register(Perfil,PerfilAdmin)
