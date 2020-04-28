from app.models import Distillery
from api.serializers import DistillerySerializer
from rest_framework import filters, permissions, viewsets


class DistilleryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows distilleries to be viewed or edited.
    """
    queryset = Distillery.objects.all()
    serializer_class = DistillerySerializer
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
