from distilleries.models import Distillery
from api.serializers import DistillerySerializer
from rest_framework import permissions
from rest_framework import viewsets


class DistilleryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows distilleries to be viewed or edited.
    """
    queryset = Distillery.objects.all()
    serializer_class = DistillerySerializer
    permission_classes = [permissions.IsAuthenticated]
