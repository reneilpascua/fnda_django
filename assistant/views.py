from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import viewsets as drf_viewsets
from rest_framework import mixins as drf_mixins
from .serializers import *
from .models import *

# Create your views here.

# class PlayerViewSet(viewsets.ModelViewSet):
class PlayerViewSet(drf_mixins.RetrieveModelMixin,
                    drf_mixins.ListModelMixin,
                    drf_viewsets.GenericViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class ZScoreSetViewSet(drf_mixins.RetrieveModelMixin,
                    drf_mixins.ListModelMixin,
                    drf_viewsets.GenericViewSet):
    queryset = ZScoreSet.objects.all()
    serializer_class = ZScoreSetSerializer

class DraftViewSet(drf_viewsets.ModelViewSet):
    queryset = Draft.objects.all()
    serializer_class = DraftSerializer

class DraftPickViewSet(drf_viewsets.ModelViewSet):
    queryset = DraftPick.objects.all()
    serializer_class = DraftPickSerializer




class TestView(TemplateView):
    template_name = 'assistant/test.html'

class PlayerListView(TemplateView):
    template_name = 'assistant/playerlist.html'

