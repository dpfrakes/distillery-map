from django.db import models
from django.contrib.gis.geos import Point
from location_field.models.spatial import LocationField

from .util import format_coordinates

class Distillery(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True)
    location = models.CharField(
        max_length=40,
        blank=True, null=True)
    region = models.CharField(
        max_length=40,
        blank=True, null=True)
    owner = models.CharField(
        max_length=60,
        blank=True, null=True)
    year_established = models.IntegerField(
        blank=True, null=True)
    year_closed = models.IntegerField(
        blank=True, null=True)
    year_demolished = models.IntegerField(
        blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=8,
        decimal_places=5,
        blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=8,
        decimal_places=5,
        blank=True, null=True)
    geolocation = LocationField(based_fields=['name'])
    image_url = models.CharField(
        max_length=200,
        blank=True, null=True)
    logo_url = models.CharField(
        max_length=200,
        blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Distilleries'

    def __str__(self):
       return self.name

    def coordinates(self):
        if self.geolocation:
            return format_coordinates(self.geolocation.x, self.geolocation.y)
        elif self.latitude and self.longitude:
            return format_coordinates(self.latitude, self.longitude)
        return '--'

# TODO make this a ManyToOne for Distillery (or individual whiskies?)
# class TasteProfile(models.Model):
#     pass
