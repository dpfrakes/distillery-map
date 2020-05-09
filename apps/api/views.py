from apps.entities.models import Distillery
from api.serializers import DistillerySerializer
from rest_framework import filters, viewsets


class DistilleryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows distilleries to be viewed or edited.
    """
    queryset = Distillery.objects.all()
    serializer_class = DistillerySerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
