from django.conf.urls.defaults import patterns, include, url
from archivo.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'correpi.views.home', name='home'),
    # url(r'^correpi/', include('correpi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^parsear/', parsear),
    url(r'^parsear2/', parsear2),

    url(r'^importar-bd/', importar_bd),
    url(r'^crear-fuerzas/', crear_fuerzas),
    url(r'^crear-circunstancias/', crear_circunstancias),
)