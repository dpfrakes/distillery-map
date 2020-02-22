from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Home page
    """
    return TemplateView.as_view(template_name='home.html')
