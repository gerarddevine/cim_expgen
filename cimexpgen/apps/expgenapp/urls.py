from django.conf.urls.defaults import *

# Enabling the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    
    (r'^ajax/modalform1$','cimexpgen.apps.expgenapp.views.modalform1', {}, 'modalform1'),
        
    #----------Experiments-------------------------------------------
    
    #experiments list page
    (r'^explist/$', 'cimexpgen.apps.expgenapp.views.explist', {}, 'explist'),
    
    #add new experiment page 
    (r'^expadd/$', 'cimexpgen.apps.expgenapp.views.expedit', {}, 'expadd'),
    
    #view experiment page 
    (r'^expview/(?P<expid>\d+)/$', 'cimexpgen.apps.expgenapp.views.expview', {}, 'expview'),
    
    #edit experiment page 
    (r'^expedit/(?P<expid>\d+)/$', 'cimexpgen.apps.expgenapp.views.expedit',{}, 'expedit'),
     
    #copy experiment page 
    (r'^expcopy/(?P<expid>\d+)/$', 'cimexpgen.apps.expgenapp.views.expcopy',{}, 'expcopy'),
                       
    #delete experiment page 
    (r'^expdelete/(?P<expid>\d+)/$', 'cimexpgen.apps.expgenapp.views.expdelete',{}, 'expdelete'),
    
    #publish experiment page 
    (r'^exppub/(?P<expid>\d+)/$', 'cimexpgen.apps.expgenapp.views.exppub',{}, 'exppub'),
    
    
    #----------Requirements---------------------------------------------
    
    #requirements list page
    (r'^reqlist/$', 'cimexpgen.apps.expgenapp.views.reqlist'),
    
    #add new requirement page 
    (r'^reqadd/$', 'cimexpgen.apps.expgenapp.views.reqedit',{}, 'reqadd'),
    
    #view requirement page 
    (r'^reqview/(?P<reqid>\d+)/$', 'cimexpgen.apps.expgenapp.views.reqview',{}, 'reqview'),
    
    #edit requirement page 
    (r'^reqedit/(?P<reqid>\d+)/$', 'cimexpgen.apps.expgenapp.views.reqedit',{}, 'reqedit'),
    
    #delete experiment page 
    (r'^reqdelete/(?P<reqid>\d+)/$', 'cimexpgen.apps.expgenapp.views.reqdelete',{}, 'reqdelete'),
    
    
    # -----------Imports---------------------------------------------- 
    
    #import cim page
    (r'^importcim/$', 'cimexpgen.apps.expgenapp.views.importcim', {}, 'import'),
        
    )

