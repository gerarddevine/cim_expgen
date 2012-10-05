'''
Created on 17 Aug 2011

@author: gerarddevine
'''

from django import forms
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

from apps.expgenapp.models import Experiment, NumericalRequirement


class ExperimentForm(ModelForm):
    class Meta:
        model = Experiment 
        widgets = {
            'requirements': CheckboxSelectMultiple(),
        }        
        
        
class RequirementForm(ModelForm):
    CHOICES = (('--------------','-------------'),
               ('BoundaryCondition','Boundary Condition'),
               ('InitialCondition','Initial Condition'),
               ('SpatioTemporalConstraint','SpatioTemporal Constraint'),)
    
    reqtype = forms.CharField(widget=forms.Select(choices=CHOICES, attrs={'size':'1'}))


    class Meta:
        model = NumericalRequirement
        
        
    def clean_reqtype(self):
        '''Check that an actual valid choice is selected'''
        reqtype = self.cleaned_data['reqtype']
        if reqtype == u'--------------':
            raise forms.ValidationError("This field is required")
          
        return reqtype 
        