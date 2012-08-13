from django.shortcuts import render_to_response, get_object_or_404 
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext

from expgenapp.models import Experiment
from expgenapp.models import NumericalRequirement
from expgenapp.forms import ExperimentForm, RequirementForm
from expgenapp.XMLutilities import getCIMXML
from expgenapp.helpers import genurls



def home(request):
    '''
    controller for app home page
    '''
    
    try:
        # get my urls
        urls = genurls()
        
        message = 'Some introductory text will go here'
        
    except:
        raise Http404
    
    return render_to_response('home.html', {'message':message, 'urls':urls}, 
                               context_instance=RequestContext(request))


def about(request):
    '''
    controller for app about page
    '''
    
    try:
        # get my urls
        urls = genurls()
        
        message = 'About page will go here'
        
    except:
        raise Http404
    
    return render_to_response('about.html', {'message':message, 'urls':urls},
                              context_instance=RequestContext(request))


def login(request):
    '''
    controller for app login page
    '''
    
    try:
        # get my urls
        urls = genurls(
                       )
        message = 'Login page will go here'
        
    except:
        raise Http404
    
    return render_to_response('login.html', {'message':message, 'urls':urls},
                              context_instance=RequestContext(request))


def modalform1(request):
    '''
    controller for app about page
    '''
    
    return render_to_response('modalform1.html', {},
                              context_instance=RequestContext(request))


def explist(request):
    '''
    controller for experiment list page .
    '''
    
    try:
        # get my urls
        urls = genurls()
        urls['modalform1']=reverse('cimexpgen.expgenapp.views.modalform1', 
                                   args=())
                
        allexps = Experiment.objects.all()
        for exp in allexps:
            exp.url = reverse('cimexpgen.expgenapp.views.expview', 
                              args=(exp.id, ))
            exp.cpurl = reverse('cimexpgen.expgenapp.views.expcopy', 
                              args=(exp.id, ))
            exp.delurl = reverse('cimexpgen.expgenapp.views.expdelete', 
                              args=(exp.id, ))
    except:
        raise Http404
    
    return render_to_response('explist.html', {'allexps':allexps, 'urls':urls}, 
                                context_instance=RequestContext(request))


def expview(request, expid):
    '''
    controller for individual experiment view page
    '''
    
    exp = get_object_or_404(Experiment, pk=expid)
    
    # get my urls
    urls = genurls()    
    urls['expedit']=reverse('cimexpgen.expgenapp.views.expedit',args=(exp.id, ))
    urls['exppub']=reverse('cimexpgen.expgenapp.views.exppub',args=(exp.id, ))
    
    #Get my numerical requirements
    reqs = NumericalRequirement.objects.filter(experiment=expid)
    
    for req in reqs:
        req.url = reverse('cimexpgen.expgenapp.views.reqview', 
                              args=(req.id, ))   
    
    #Send to template
    return render_to_response('expview.html', 
                              {'exp': exp, 'urls':urls, 'reqs':reqs},
                                context_instance=RequestContext(request))


def expcopy(request, expid):
    '''
    controller for individual experiment copy page
    '''
    
    exp = get_object_or_404(Experiment, pk=expid)
    
    # get my urls
    urls = genurls() 
    urls['expedit']=reverse('cimexpgen.expgenapp.views.expedit',args=(exp.id, ))
    urls['exppub']=reverse('cimexpgen.expgenapp.views.exppub',args=(exp.id, ))
    
    return HttpResponseRedirect(urls['explist']) # Redirect after POST


def expdelete(request, expid):
    '''
    controller for individual experiment delete page
    '''
    
    # get my urls
    urls = genurls()
    
    exp = get_object_or_404(Experiment, pk=expid)
    exp.delete()
    
    return HttpResponseRedirect(urls['explist']) # Redirect after POST
         

def expedit(request, expid=None):
    '''
    controller for individual experiment edit page
    '''
    
    if expid:
        exp = get_object_or_404(Experiment, pk=expid)
    else: 
        exp = Experiment()
        
    
    # get my urls
    urls = genurls()
    
    # Deal with response 
    if request.method == 'POST':
        cancel = request.POST.get('cancel', None)
        if cancel:
            return HttpResponseRedirect(urls['explist'])
        else:
            #urls['self']=reverse('cimexpgen.expgenapp.views.expedit', args=(exp.id, )) 
        
            if 'expform' in request.POST:
                expform = ExperimentForm(request.POST, instance=exp, prefix='exp') 
                if expform.is_valid(): 
                    expform.save()   
            
                return HttpResponseRedirect(urls['explist']) # Redirect to list page
            elif 'reqform' in request.POST:
                reqform = RequirementForm(request.POST, 
                                          instance=NumericalRequirement(), 
                                          prefix='req') 
                if reqform.is_valid(): 
                    newreq = reqform.save()
                    exp.requirements.add(newreq)
            
                return HttpResponseRedirect(urls['explist']) # Redirect to list page
    else:
        expform = ExperimentForm(instance=exp, prefix='exp') # An unbound form
        reqform = RequirementForm(prefix='req') # An unbound form

    return render_to_response('expedit.html', 
                              {'expform': expform,               
                               'reqform': reqform, 
                               'urls':urls},
                                context_instance=RequestContext(request))

#    # Deal with response 
#    if request.method == 'POST': 
#        form = ExperimentForm(request.POST, instance=exp) 
#        if form.is_valid(): 
#            form.save()   
#        
#            return HttpResponseRedirect(urls['explist']) # Redirect to list page
#    else:
#        form = ExperimentForm(instance=exp) # An unbound form
#        
#
#    return render_to_response('expedit.html', {'form': form, 'urls':urls},
#                                context_instance=RequestContext(request))


def exppub(request, expid):
    '''
    controller for individual experiment publish page
    '''
    # generate xml instance of self
    cim = getCIMXML(expid)
    
    mimetype='application/xml'
    return HttpResponse(cim, mimetype)
    

def reqlist(request):
    '''
    controller for requirement list page
    '''
    
    try:        
        allreqs = NumericalRequirement.objects.all()
        for req in allreqs:
            req.url = reverse('cimexpgen.expgenapp.views.reqview', 
                              args=(req.id, ))
            req.delurl = reverse('cimexpgen.expgenapp.views.reqdelete', 
                              args=(req.id, ))
        
        # get my urls
        urls = genurls()
        
    except:
        raise Http404
    
    return render_to_response('reqlist.html', {'allreqs':allreqs, 'urls':urls}, 
                                       context_instance=RequestContext(request))



def reqview(request, reqid):
    '''
    controller for individual requirement view page
    '''
    
    req = get_object_or_404(NumericalRequirement, pk=reqid)
    
    # get my urls
    urls = genurls()
    urls['reqedit']=reverse('cimexpgen.expgenapp.views.reqedit',args=(req.id, ))
         
    return render_to_response('reqview.html', {'req':req, 'urls':urls}, 
                                context_instance=RequestContext(request))



def reqedit(request, reqid=None):
    '''
    controller for individual numerical requirement edit page
    '''
    
    if reqid:
        req = get_object_or_404(NumericalRequirement, pk=reqid)
    else:
        req = NumericalRequirement()  
    
    # get my urls
    urls = genurls()  
          
    if request.method == 'POST': 
        cancel = request.POST.get('cancel', None)
        if cancel:
            return HttpResponseRedirect(urls['reqlist'])
        else:
            form = RequirementForm(request.POST, instance=req)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(urls['reqlist']) # Redirect after POST
    else:
        form = RequirementForm(instance=req) # An unbound form

    return render_to_response('reqedit.html', {'form': form, 'urls':urls}, 
                                context_instance=RequestContext(request))


def reqdelete(request, reqid=None):
    '''
    controller for deleting an individual requirement
    '''
    
    req = get_object_or_404(NumericalRequirement, pk=reqid)
    req.delete()
    
    # get my urls
    urls = genurls()

    # Redirect after POST
    return HttpResponseRedirect(urls['reqlist'])


def importcim(request):
    '''
    controller for importing CIM document
    '''
    
    try:        
        message = 'Import CIM page will go here'
        # get my urls
        urls = genurls()
        
    except:
        raise Http404
    
    return render_to_response('importcim.html', 
                              {'message':message, 'urls':urls})