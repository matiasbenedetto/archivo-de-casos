from django.contrib import admin
from models import *

admin.site.register(Fuerza)
admin.site.register(Circunstancia)
admin.site.register(Archivodecasos)

class CasoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'edad', 'sexo', 'provincia', 'fecha_deceso')
    list_editable = ('sexo',) 
admin.site.register(Caso, CasoAdmin)
