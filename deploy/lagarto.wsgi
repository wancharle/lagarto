import os, sys
sys.path.append('/home/rabodolagarto/apps_wsgi/lagarto')
sys.path.append('/home/rabodolagarto/apps_wsgi/lagarto/lagarto')
os.environ['PYTHON_EGG_CACHE'] = '/home/rabodolagarto/apps_wsgi/.python-eggs'
os.environ['DJANGO_SETTINGS_MODULE']='lagarto.settings.local'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
