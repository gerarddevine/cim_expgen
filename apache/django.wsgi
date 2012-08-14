# This application object is used by the development server
# as well as any WSGI server configured to use this file.

import os, sys
sys.path.append('/home/gdevine/dev/django')
os.environ['DJANGO_SETTINGS_MODULE'] = 'cim_expgen.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

