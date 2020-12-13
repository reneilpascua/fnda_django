from django.conf.urls import url
from .views import TestView, PlayerListView


urlpatterns = [
    url(r'^test/', TestView.as_view()),
    url(r'^players/', PlayerListView.as_view())
]
