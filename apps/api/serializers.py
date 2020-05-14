from apps.entities.models import Company, Distillery

from rest_framework import serializers

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    latitude = serializers.ReadOnlyField()
    longitude = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = ['name', 'latitude', 'longitude']

class DistillerySerializer(serializers.HyperlinkedModelSerializer):
    latitude = serializers.ReadOnlyField()
    longitude = serializers.ReadOnlyField()
    owner = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Distillery
        fields = ['name', 'region', 'owner', 'year_established',
          'year_closed', 'year_demolished', 'latitude', 'longitude',
          'geolocation', 'image', 'logo_url']
