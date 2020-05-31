from django.conf.urls import url
from .views import *

app_name = 'course'

urlpatterns = [
    url(r'^index/$', course_index, name='index'),
    url(r'^(?P<id>\d+)/$', course_detail, name='detail'),
    url(r'^create/$', course_create, name='create'),
    url(r'^(?P<id>\d+)/update/$', course_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', course_delete, name='delete'),
]