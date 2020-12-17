from django.conf.urls import url
from knox import views as knox_views
from .views import RegisterUserAPIView, LoginAPIView

urlpatterns = [
    url(r'^register/$', RegisterUserAPIView.as_view(), name='register-user'),
    url(r'^login/$', LoginAPIView.as_view(), name='login'),
    url(r'^logout/$', knox_views.LogoutView.as_view(), name='logout'),
    url(r'^logout-all/$', knox_views.LogoutAllView.as_view(), name='logout-all'),
]