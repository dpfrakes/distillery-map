from django.db import models


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

    class Meta:
        verbose_name_plural = 'Distilleries'

    def __str__(self):
       return self.name

    def coordinates(self):
        if self.latitude and self.longitude:
            lat_deg = int(self.latitude)
            lat_min = abs(int((self.latitude % 1) * 60))
            lat_sec = abs(int((((self.latitude % 1) * 60) % 1) * 60))
            lng_deg = int(self.longitude)
            lng_min = abs(int((self.longitude % 1) * 60))
            lng_sec = abs(int((((self.longitude % 1) * 60) % 1) * 60))
            return f'{lat_deg}°{lat_min}\'{lat_sec}" {lng_deg}°{lng_min}\'{lng_sec}" '
        return '--'

# TODO make this a ManyToOne for Distillery (or individual whiskies?)
# class TasteProfile(models.Model):
#     pass
