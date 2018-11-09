from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html' # this is passed to urls.py

class AboutPageView(TemplateView):
    template_name = 'about.html'