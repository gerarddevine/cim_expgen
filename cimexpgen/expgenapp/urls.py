from django.conf.urls.defaults import *

# Enabling the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                       
    #----------Admin-------------------------------------------------                       
    
    url(r'^cimexpgen/admin/', include(admin.site.urls)),                      
    
    
    #----------General-----------------------------------------------
    
    #home page
    (r'^$','cimexpgen.expgenapp.views.home', {}, 'home'),
    (r'^cimexpgen/$','cimexpgen.expgenapp.views.home', {}, 'home'),
    
    #help page
    (r'^cimexpgen/about/$','cimexpgen.expgenapp.views.about', {}, 'about'),
    
    #login page
    (r'^cimexpgen/login/$','cimexpgen.expgenapp.views.login', {}, 'login'),
    
    (r'^ajax/modalform1$','cimexpgen.expgenapp.views.modalform1', {}, 'modalform1'),
        
    #----------Experiments-------------------------------------------
    
    #experiments list page
    (r'^cimexpgen/explist/$', 
     'cimexpgen.expgenapp.views.explist', {}, 'explist'),
    
    #add new experiment page 
    (r'^cimexpgen/expadd/$', 
     'cimexpgen.expgenapp.views.expedit',{}, 'expadd'),
    
    #view experiment page 
    (r'^cimexpgen/expview/(?P<expid>\d+)/$', 
     'cimexpgen.expgenapp.views.expview', {}, 'expview'),
    
    #edit experiment page 
    (r'^cimexpgen/expedit/(?P<expid>\d+)/$', 
     'cimexpgen.expgenapp.views.expedit',{}, 'expedit'),
     
    #copy experiment page 
    (r'^cimexpgen/expcopy/(?P<expid>\d+)/$', 
     'cimexpgen.expgenapp.views.expcopy',{}, 'expcopy'),
                       
    #delete experiment page 
    (r'^cimexpgen/expdelete/(?P<expid>\d+)/$', 
     'cimexpgen.expgenapp.views.expdelete',{}, 'expdelete'),
    
    #publish experiment page 
    (r'^cimexpgen/exppub/(?P<expid>\d+)/$', 
     'cimexpgen.expgenapp.views.exppub',{}, 'exppub'),
    
    
    #----------Requirements---------------------------------------------
    
    #requirements list page
    (r'^cimexpgen/reqlist/$', 
     'cimexpgen.expgenapp.views.reqlist'),
    
    #add new requirement page 
    (r'^cimexpgen/reqadd/$', 
     'cimexpgen.expgenapp.views.reqedit',{}, 'reqadd'),
    
    #view requirement page 
    (r'^cimexpgen/reqview/(?P<reqid>\d+)/$', 
     'cimexpgen.expgenapp.views.reqview',{}, 'reqview'),
    
    #edit requirement page 
    (r'^cimexpgen/reqedit/(?P<reqid>\d+)/$', 
     'cimexpgen.expgenapp.views.reqedit',{}, 'reqedit'),
    
    #delete experiment page 
    (r'^cimexpgen/reqdelete/(?P<reqid>\d+)/$', 
     'cimexpgen.expgenapp.views.reqdelete',{}, 'reqdelete'),
    
    
    # -----------Imports---------------------------------------------- 
    
    #import cim page
    (r'^cimexpgen/importcim/$', 
     'cimexpgen.expgenapp.views.importcim', {}, 'import'),
        
    )

