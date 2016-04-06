# coding=utf-8
import os
import sys
root = os.path.dirname(os.path.dirname(__file__))                                            
sys.path.insert(0, os.path.join(root, 'site-packages'))               
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "zjwebsite.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()