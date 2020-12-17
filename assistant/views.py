from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class TestView(TemplateView):
    template_name = 'assistant/test.html'

class PlayerListView(TemplateView):
    template_name = 'assistant/playerlist.html'