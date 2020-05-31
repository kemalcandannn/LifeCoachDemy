from django.conf.urls import url
from .views import *

app_name = 'project'

urlpatterns = [
    url(r'^index/$', project_index, name='index'),
    url(r'^create/$', project_create, name='create'),

    url(r'^(?P<slug>[\w-]+)/$', project_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', project_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', project_delete, name='delete'),
]