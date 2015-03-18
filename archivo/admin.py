from django.contrib import admin
from models import *

admin.site.register(Fuerza)
admin.site.register(Circunstancia)
admin.site.register(Archivodecasos)
admin.site.register(TipoEdad)

class CasoAdmin(admin.ModelAdmin):
	list_display_links=('nombre', 'apellido')
	list_display = ('foto', 'id', 'nombre', 'apellido', 'edad', 'sexo', 'provincia', 'fecha_deceso')
	list_editable = ('sexo',)
	search_fields = ['nombre', 'apellido', 'edad', 'provincia']
	list_filter = ['sexo', 'provincia', 'circunstancia', 'fuerza']

admin.site.register(Caso, CasoAdmin)
