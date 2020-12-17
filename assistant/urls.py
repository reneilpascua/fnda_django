from django.conf.urls import url, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('players', PlayerViewSet)
router.register('zscores', ZScoreSetViewSet)
router.register('drafts', DraftViewSet)
router.register('draft-picks', DraftPickViewSet)

urlpatterns = [
    url(r'^test/', TestView.as_view()),
    # url(r'^players/', PlayerListView.as_view())
]
urlpatterns += router.urls
