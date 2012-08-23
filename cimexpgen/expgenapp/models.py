from lxml import etree as ET

#from cimexpgen.expgenapp.XMLGen import XMLGenerator

from django.db import models

  
class Experiment(models.Model):
    '''Class to represent numericalExperiment 

    '''
    
    abbrev = models.CharField(max_length=40)
    title = models.CharField(max_length=128, blank=True, null=True)
    author = models.CharField(max_length=64, blank=True, null=True)
    project = models.CharField(max_length=64, blank=True, null=True)
    control = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    rationale = models.TextField(blank=True, null=True)
    requirements = models.ManyToManyField('NumericalRequirement', blank=True, 
                                          null=True)   
    # These are added automatically
    created = models.DateField(auto_now_add=True, editable=False)
    updated = models.DateField(auto_now=True, editable=False)
    
    
    def __unicode__(self):
        return self.abbrev
   
    def xmlobject(self):
        ''' Return an lxml object view of me '''
        #CIMxml = XMLGenerator()
        #return CIMxml.generateXML(self)
    
    def gencimxml(self):
        ''' 
        Generate an xml instance string of myself 
        '''
       
        return ET.tostring(self.xmlobject(), pretty_print=True)    
        

class NumericalRequirement(models.Model):
    '''Class to represent a numerical requirement

    '''
    
    docid = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=128)
    reqtype = models.CharField(max_length=32)
    # These are added automatically
    created = models.DateField(auto_now_add=True, editable=False)
        
    def __unicode__(self):
        return self.name
    

class RequirementOption(models.Model):
    ''' Class to represent a numerical requirement option

    '''
    
    docid = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    name = models.CharField(max_length=128)
    # These are added automatically
    created = models.DateField(auto_now_add=True, editable=False)
        
    def __unicode__(self):
        return self.name
