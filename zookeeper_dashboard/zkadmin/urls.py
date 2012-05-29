from django.conf.urls import *

urlpatterns = patterns('zookeeper_dashboard.zkadmin.views',
    (r'^server/(?P<server_id>\d+)/$','detail'), 
    (r'^$','index'), 
)
