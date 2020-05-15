from apps.entities.models import Company, Distillery

from rest_framework import serializers

class DistillerySerializer(serializers.ModelSerializer):
    latitude = serializers.ReadOnlyField()
    longitude = serializers.ReadOnlyField()
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Distillery
        fields = ['name', 'region', 'owner', 'year_established',
          'year_closed', 'year_demolished', 'latitude', 'longitude',
          'image', 'logo_url']

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    latitude = serializers.ReadOnlyField()
    longitude = serializers.ReadOnlyField()
    distilleries = DistillerySerializer(many=True)

    class Meta:
        model = Company
        fields = ['name', 'latitude', 'longitude', 'distilleries']
