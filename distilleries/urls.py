from django.urls import path, include
from rest_framework import routers

from . import views
from api import views as api_views

router = routers.DefaultRouter()
router.register(r'distilleries', api_views.DistilleryViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api', include('rest_framework.urls', namespace='rest_framework')),
]
