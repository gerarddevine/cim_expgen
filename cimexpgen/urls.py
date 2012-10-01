from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                           
    # admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # home and about pages
    (r'^$','cimexpgen.apps.expgenapp.views.home', {}, 'home'),
    (r'^home/$','cimexpgen.apps.expgenapp.views.home', {}, 'home'),
    (r'^about/$','cimexpgen.apps.expgenapp.views.about', {}, 'about'),
        
    #url for user registration/login/logour
    (r'^register/$', 'cimexpgen.apps.person.views.UserRegistration'),
    (r'^login/$', 'cimexpgen.apps.person.views.LoginRequest', {}, 'login'),
    (r'^logout/$', 'cimexpgen.apps.person.views.LogoutRequest', {}, 'logout'),
    
    # including app level urls.py's
    (r'', include('cimexpgen.apps.expgenapp.urls')),
    (r'', include('cimexpgen.apps.person.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^static/(?P<path>.*)$', 
        'serve', {
        'document_root': settings.STATIC_ROOT,
        'show_indexes': True }),
    (r'^media/(?P<path>.*)$', 
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),
    )