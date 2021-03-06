from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
    
    #acciones sobre base de datos
    #url(r'^actualizar-bd/', actualizar_bd),
    #url(r'^importar-bd/', importar_bd),
    #url(r'^crear-fuerzas/', crear_fuerzas),
    #url(r'^crear-circunstancias/', crear_circunstancias),
    #url(r'^crear-tipo-edad/', crear_tipo_edad),
    #url(r'^buscar-coordenadas/', buscar_coordenadas),

    url(r'^casos-sin-coordenadas/', casos_sin_coordenadas),
    

    #--------------------------------
    url(r'^caso/([a-zA-Z0-9_-]+)/$', caso),
    url(r'^caso-json/$', caso_json),
    url(r'^mapa/', mapa),
    url(r'^cargar-marcadores/', cargar_marcadores),
    url(r'^buscar/', buscar),

    url(r'^los-muertos-de-2001/', los_muertos_de_2001),

    #paginas
    url(r'^que-es/', que_es),
    url(r'^sumate/', sumate),



    
)