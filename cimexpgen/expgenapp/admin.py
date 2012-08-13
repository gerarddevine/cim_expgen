'''

Admin functionality

Created on 26 Aug 2011

@author: gerarddevine
'''

from cimexpgen.expgenapp.models import Experiment, NumericalRequirement
from django.contrib import admin

admin.site.register(Experiment)
admin.site.register(NumericalRequirement)


