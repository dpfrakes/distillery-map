from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse

import json

from .models import Distillery


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        distilleries = Distillery.objects.filter(latitude__isnull=False).filter(longitude__isnull=False)
        context['distilleries'] = list(map(lambda d: {
                'name': d.name,
                'coordinates': [float(d.longitude), float(d.latitude)],
                'region': d.region or 'Other',
                'year_established': d.year_established or 'Unknown',
            }, distilleries))
        print()
        print()
        print('*' * 80)
        print(context)
        print('*' * 80)
        print()
        print()
        # name: '{{ distillery.name }}',
        # coordinates: [parseFloat('{{ distillery.longitude }}'), parseFloat('{{ distillery.latitude }}')],
        # region: '{{ distillery.region|default:"Other" }}',
        # year_established: '{{ distillery.year_established|default:"Unknown" }}',

        return context
