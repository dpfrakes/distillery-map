from django.db import models


class Distillery(models.Model):
    name = models.CharField(
        max_length=50,
        blank=True, null=True)
    location = models.CharField(
        max_length=40,
        blank=True, null=True)
    region = models.CharField(
        max_length=40,
        blank=True, null=True)
    owner = models.CharField(
        max_length=60,
        blank=True, null=True)
    latitude = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True, null=True)
    longitude = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True, null=True)

    class Meta:
    	verbose_name_plural = 'Distilleries'
