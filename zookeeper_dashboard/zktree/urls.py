from django.conf.urls import *

urlpatterns = patterns('zookeeper_dashboard.zktree.views',
    (r'^(?P<path>.*)/$','index'), 
    (r'^$','index'), 
    (r'^delete$','delete'), 
)
