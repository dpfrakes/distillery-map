from apps.api.serializers import CompanySerializer, DistillerySerializer
from apps.entities.models import Company, Distillery
from rest_framework import filters, viewsets


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)

class DistilleryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows distilleries to be viewed or edited.
    """
    queryset = Distillery.objects.all()
    serializer_class = DistillerySerializer
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
