from django.contrib import admin
from models import Caso

#admin.site.register(Caso)


class CasoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'edad', 'sexo', 'provincia', 'fecha_deceso')
    list_editable = ('sexo',) 
admin.site.register(Caso, CasoAdmin)