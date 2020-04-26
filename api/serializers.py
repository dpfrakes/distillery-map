from distilleries.models import Distillery

from rest_framework import serializers


class DistillerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Distillery
        fields = ['name', 'region', 'owner', 'year_established',
          'year_closed', 'year_demolished', 'geolocation']
