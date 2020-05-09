from entities.models import Distillery

from rest_framework import serializers


class DistillerySerializer(serializers.HyperlinkedModelSerializer):
    latitude = serializers.ReadOnlyField()
    longitude = serializers.ReadOnlyField()
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Distillery
        fields = ['name', 'region', 'owner', 'year_established',
          'year_closed', 'year_demolished', 'latitude', 'longitude',
          'geolocation', 'image', 'logo_url']
