from django.shortcuts import render

from entities.models import Distillery


def distillery_detail(request, slug):
    template_name = 'distillery/detail.html'
    context = {
        'distillery': Distillery.objects.get(slug=slug)
    }
    return render(request, template_name, context)
