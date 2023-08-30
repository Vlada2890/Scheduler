from django.shortcuts import render
from django.views import TemplateView


class HomeView(TemplateView):
    template_name = "index.html"