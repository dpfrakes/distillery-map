"""distillery-map URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from rest_framework import routers

from api import views as api_views
from entities.views import distillery_detail

router = routers.DefaultRouter()
router.register(r'distilleries', api_views.DistilleryViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),

    # Temporary URL for detail page (to be done with React/Redux later)
    path('distillery/<slug:slug>/', distillery_detail),
]
