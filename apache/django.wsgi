import os, sys
sys.path.append('/home/ubuntu/zookeeper_dashboard')
os.environ['DJANGO_SETTINGS_MODULE'] = 'zookeeper_dashboard.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
