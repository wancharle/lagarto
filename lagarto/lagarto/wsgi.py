import os
import sys
import site

# Tell wsgi to add the Python site-packages to its path. 
site.addsitedir('/home/wancharle/.virtualenvs/lagarto/lib/python2.7/site-packages')


activate_this = os.path.expanduser("~/.virtualenvs/lagarto/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# Calculate the path based on the location of the WSGI script
project = '/home/wancharle/webapps/lagarto/lagarto/'
workspace = os.path.dirname(project)
sys.path.append(workspace)

os.environ['DJANGO_SETTINGS_MODULE'] = 'lagarto.settings.local'
from django.core.handlers.wsgi import WSGIHandler

application = WSGIHandler()
