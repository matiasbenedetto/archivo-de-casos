from django.conf.urls import patterns, include, url
from views import *


urlpatterns = patterns('',
    
    url(r'^importar-bd/', importar_bd),
    url(r'^crear-fuerzas/', crear_fuerzas),
    url(r'^crear-circunstancias/', crear_circunstancias),
    url(r'^buscar-coordenadas/', buscar_coordenadas),
    url(r'^cargar-marcadores/', cargar_marcadores),
    
)