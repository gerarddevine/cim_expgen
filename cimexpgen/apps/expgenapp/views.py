from django.shortcuts import render_to_response, get_object_or_404 
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

from guardian.shortcuts import assign
from guardian.decorators import permission_required_or_403

from apps.expgenapp.models import Experiment
from apps.expgenapp.models import NumericalRequirement
from apps.expgenapp.forms import ExperimentForm, RequirementForm
from apps.expgenapp.XMLutilities import getCIMXML

from apps.helpers import genurls


def home(request):
    '''Controller for app home page
    '''
    try:
        # get my urls
        urls = genurls()
    except:
        raise Http404
    
    return render_to_response('page/home.html', {'urls': urls},
                              context_instance=RequestContext(request))


def about(request):
    '''Controller for app about page
    '''
    try:
        # get my urls
        urls = genurls()
    except:
        raise Http404
      
    return render_to_response('page/about.html', {'urls': urls},
                              context_instance=RequestContext(request))


# TODO: link this to the template
def modalform1(request):
    '''
    controller for app about page
    '''
    return render_to_response('page/modalform1.html', {},
                              context_instance=RequestContext(request))


@login_required
def explist(request):
    '''
    controller for experiment list page .
    '''
    try:
        # get my urls
        urls = genurls()
        urls['modalform1'] = reverse('cimexpgen.apps.expgenapp.views.modalform1',
                                   args=())
        allexps = Experiment.objects.filter(author=request.user)
        for exp in allexps:
            exp.url = reverse('cimexpgen.apps.expgenapp.views.expview',
                              args=(exp.id, ))
            exp.cpurl = reverse('cimexpgen.apps.expgenapp.views.expcopy',
                              args=(exp.id, ))
            exp.delurl = reverse('cimexpgen.apps.expgenapp.views.expdelete',
                              args=(exp.id, ))
    except:
        raise Http404
    return render_to_response('page/explist.html', {'allexps': allexps,
                                               'urls': urls},
                                context_instance=RequestContext(request))


@login_required
@permission_required_or_403('expgenapp.manage_exp', (Experiment, 'id', 'expid'))
def expview(request, expid):
    '''
    controller for individual experiment view page
    '''    
    exp = get_object_or_404(Experiment, pk=expid)
    
    # get my urls
    urls = genurls()    
    urls['expedit']=reverse('cimexpgen.apps.expgenapp.views.expedit',args=(exp.id, ))
    urls['exppub']=reverse('cimexpgen.apps.expgenapp.views.exppub',args=(exp.id, ))
    
    #Get my numerical requirements
    reqs = NumericalRequirement.objects.filter(experiment=expid)
    
    for req in reqs:
        req.url = reverse('cimexpgen.apps.expgenapp.views.reqview', 
                              args=(req.id, ))   
    
    #Send to template
    return render_to_response('page/expview.html', 
                              {'exp': exp, 'urls':urls, 'reqs':reqs},
                                context_instance=RequestContext(request))


@login_required
@permission_required_or_403('expgenapp.manage_exp', (Experiment, 'id', 'expid'))
def expcopy(request, expid):
    '''
    controller for individual experiment copy page
    '''
    
    exp = get_object_or_404(Experiment, pk=expid)
    
    # get my urls
    urls = genurls() 
    urls['expedit']=reverse('cimexpgen.apps.expgenapp.views.expedit',args=(exp.id, ))
    urls['exppub']=reverse('cimexpgen.apps.expgenapp.views.exppub',args=(exp.id, ))
    
    return HttpResponseRedirect(urls['explist']) # Redirect after POST


@login_required
@permission_required_or_403('expgenapp.manage_exp', (Experiment, 'id', 'expid'))
def expdelete(request, expid):
    '''
    controller for individual experiment delete page
    '''
    
    # get my urls
    urls = genurls()
    
    exp = get_object_or_404(Experiment, pk=expid)
    exp.delete()
    
    return HttpResponseRedirect(urls['explist']) # Redirect after POST
  

@login_required
def expadd(request):
    '''
    controller for experiment add page
    '''
    
    exp = Experiment()
        
    # get my urls
    urls = genurls()
    
    # Deal with response 
    if request.method == 'POST':
        cancel = request.POST.get('cancel', None)
        if cancel:
            return HttpResponseRedirect(urls['explist'])
        else:        
            if 'expform' in request.POST:
                expform = ExperimentForm(request.POST, instance=exp, prefix='exp') 
                if expform.is_valid(): 
                    exp = expform.save(commit=False)
                    exp.author = request.user
                    exp.save()
                    # assign permissions to access this experiment
                    assign('manage_exp', request.user, exp)
                    
                    return HttpResponseRedirect(urls['explist']) # Redirect to list page 
                else:
                    return render_to_response('page/expedit.html', {'expform': expform, 'urls':urls}, context_instance=RequestContext(request))
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

    return render_to_response('page/expedit.html', 
                              {'expform': expform,               
                               'reqform': reqform, 
                               'urls':urls},
                                context_instance=RequestContext(request))



@login_required
@permission_required_or_403('expgenapp.manage_exp', (Experiment, 'id', 'expid'))
def expedit(request, expid=None):
    '''
    controller for individual experiment edit page
    '''
    
    exp = get_object_or_404(Experiment, pk=expid)
        
    # get my urls
    urls = genurls()
    
    # Deal with response 
    if request.method == 'POST':
        cancel = request.POST.get('cancel', None)
        if cancel:
            # reroute back to view page
            urls['expview']=reverse('cimexpgen.apps.expgenapp.views.expview',args=(exp.id, ))
            return HttpResponseRedirect(urls['expview'])
        else:        
            if 'expform' in request.POST:
                expform = ExperimentForm(request.POST, instance=exp, prefix='exp') 
                if expform.is_valid(): 
                    exp = expform.save(commit=False)
                    exp.author = request.user
                    exp.save()
                    # assign permissions to access this experiment
                    assign('manage_exp', request.user, exp)
                    
                    return HttpResponseRedirect(urls['explist']) # Redirect to list page 
                else:
                    return render_to_response('page/expedit.html', {'expform': expform, 'urls':urls}, context_instance=RequestContext(request))
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

    return render_to_response('page/expedit.html', 
                              {'expform': expform,               
                               'reqform': reqform, 
                               'urls':urls},
                                context_instance=RequestContext(request))


@login_required
@permission_required_or_403('expgenapp.manage_exp', (Experiment, 'id', 'expid'))
def exppub(request, expid):
    '''
    controller for individual experiment publish page
    '''
    # generate xml instance of self
    cim = getCIMXML(expid)
    
    mimetype='application/xml'
    return HttpResponse(cim, mimetype)
    

@login_required
def reqlist(request):
    '''
    controller for requirement list page
    '''
    
    try:        
        allreqs = NumericalRequirement.objects.all()
        for req in allreqs:
            req.url = reverse('cimexpgen.apps.expgenapp.views.reqview', 
                              args=(req.id, ))
            req.delurl = reverse('cimexpgen.apps.expgenapp.views.reqdelete', 
                              args=(req.id, ))
        
        # get my urls
        urls = genurls()
        
    except:
        raise Http404
    
    return render_to_response('page/reqlist.html', {'allreqs':allreqs, 'urls':urls}, 
                                       context_instance=RequestContext(request))


@login_required
def reqview(request, reqid):
    '''
    controller for individual requirement view page
    '''
    
    req = get_object_or_404(NumericalRequirement, pk=reqid)
    
    # get my urls
    urls = genurls()
    urls['reqedit']=reverse('cimexpgen.apps.expgenapp.views.reqedit',args=(req.id, ))
         
    return render_to_response('page/reqview.html', {'req':req, 'urls':urls}, 
                                context_instance=RequestContext(request))


@login_required
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
            if reqid:  # reroute back to view page
                urls['reqview']=reverse('cimexpgen.apps.expgenapp.views.reqview', args=(req.id, ))
                return HttpResponseRedirect(urls['reqview'])
            else:  # reroute back to req list page
                return HttpResponseRedirect(urls['reqlist'])
        else:          
            reqform = RequirementForm(request.POST, instance=req)
            if reqform.is_valid():
                reqform.save()
                return HttpResponseRedirect(urls['reqlist']) # Redirect after POST
            else:
                return render_to_response('page/reqedit.html', {'reqform': reqform, 'urls':urls}, context_instance=RequestContext(request))
    else:
        reqform = RequirementForm(instance=req) # An unbound form

    return render_to_response('page/reqedit.html', {'reqform': reqform, 'urls':urls}, 
                                context_instance=RequestContext(request))


@login_required
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


@login_required
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
    
    return render_to_response('page/importcim.html', 
                              {'message':message, 'urls':urls})
    
