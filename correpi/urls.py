from django.conf.urls import patterns, include, url
from archivo.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'correpi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^parsear/', parsear),
    url(r'^parsear2/', parsear2),

    url(r'^importar-bd/', importar_bd),
    url(r'^crear-fuerzas/', crear_fuerzas),
    url(r'^crear-circunstancias/', crear_circunstancias),
)
