from django.conf.urls import url
from .views import *

app_name = 'contact'

urlpatterns = [
    url(r'^index/$', contact_index, name='index'),
    url(r'^create/$', contact_create, name='create'),

    url(r'^(?P<slug>[\w-]+)/$', contact_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', contact_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', contact_delete, name='delete'),
]