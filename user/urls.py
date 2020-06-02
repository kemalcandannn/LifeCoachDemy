from django.conf.urls import url
from .views import *

app_name = 'user'

urlpatterns = [
    url(r'^index/$', user_index, name='index'),
    url(r'^create/$', user_create, name='create'),

    url(r'^(?P<slug>[\w-]+)/$', user_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', user_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', user_delete, name='delete'),
]