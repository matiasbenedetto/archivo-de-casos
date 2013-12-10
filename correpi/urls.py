from django.conf.urls import patterns, include, url
from archivo.views import index

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'correpi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),



    (r'^$', index),

    (r'^archivo/', include('archivo.urls')),

    ('^accounts/', include('django.contrib.auth.urls')),

)
