from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^testbase/$', views.testBase, name='test-base'),
    url(r'^testid/(?P<id>[0-9]+)/$', views.testId, name='test-id'),
]