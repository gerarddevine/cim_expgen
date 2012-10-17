'''

Helper class for experiment generator application

Created on 13 Aug 2012

@author: gerarddevine
'''

from django.core.urlresolvers import reverse


# set up generic urls
def genurls():
    '''Create a dictionary of general URL reversals
    
    '''
    
    urls = {}
    urls['home'] = reverse('home', args=())
    urls['about'] = reverse('about', args=())
    urls['login'] = reverse('login', args=())
    urls['logout'] = reverse('logout', args=())
    urls['register'] = reverse('register', args=())
    urls['explist'] = reverse('explist', args=())
    urls['expadd'] = reverse('expadd', args=())
    urls['reqlist'] = reverse('reqlist', args=())
    urls['reqadd'] = reverse('reqadd', args=())
    urls['importcim'] = reverse('cimexpgen.apps.expgenapp.views.importcim', args=())
    
    return urls