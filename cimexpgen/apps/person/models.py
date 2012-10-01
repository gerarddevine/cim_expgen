from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Person(models.Model):
    ''' Class to represent a user profile '''
    
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    institute = models.CharField(max_length=512)
    
    def __unicode__(self):
        return self.name
    

#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        Person.objects.create(user=instance)
#
#post_save.connect(create_user_profile, sender=User)