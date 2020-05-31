from django.conf.urls import url
from .views import *

app_name = 'course'

urlpatterns = [
    url(r'^index/$', course_index, name='index'),
    url(r'^create/$', course_create, name='create'),

    url(r'^(?P<slug>[\w-]+)/$', course_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', course_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', course_delete, name='delete'),
]