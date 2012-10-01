'''
Created on 17 Aug 2011

@author: gerarddevine
'''

from django.forms import ModelForm
from django import forms

from apps.expgenapp.models import Experiment, NumericalRequirement


class ExperimentForm(ModelForm):
    class Meta:
        model = Experiment 
        
        
class RequirementForm(ModelForm):
    CHOICES = (('--------------','-------------'),
               ('BoundaryCondition','Boundary Condition'),
               ('InitialCondition','Initial Condition'),
               ('SpatioTemporalConstraint','SpatioTemporal Constraint'),)
    
    reqtype = forms.CharField(widget=forms.Select(choices=CHOICES, attrs={'size':'1'}))

    class Meta:
        model = NumericalRequirement 
        