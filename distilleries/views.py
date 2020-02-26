from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

from .models import Distillery


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        distilleries = Distillery.objects.filter(latitude__isnull=False).filter(longitude__isnull=False)
        context['distilleries'] = distilleries
        return context
