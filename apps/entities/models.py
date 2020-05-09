from django.conf import settings
from django.contrib.gis.geos import Point
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify

from django_countries.fields import CountryField
from location_field.models.spatial import LocationField

from apps.pricing.models import VirginiaPriceInfo
from .util import format_coordinates


class Company(models.Model):
    name = models.CharField(
        max_length=50, unique=True)
    # hq_location = LocationField(
    #     blank=True, null=True)
    country = CountryField(
        blank=True, null=True)
    notes = models.TextField(
        blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Companies'

    def __str__(self):
       return self.name

    def owned_properties(self):
        try:
            distilleries = Distillery.objects.filter(owner=self).order_by('name')
            distillery_list = [f'<a href="{reverse("admin:entities_distillery_change", args=[d.pk])}">{d.name}</a>' for d in distilleries]
            return format_html('<br/>'.join(distillery_list))
        except Exception as e:
            return ''
    owned_properties.short_description = 'Distilleries'

    @property
    def flag(self):
        return format_html('<img src="' + self.country.flag + '"/>')

class Distillery(models.Model):
    name = models.CharField(
        max_length=50, unique=True)
    slug = models.SlugField(
        blank=True, null=True)
    location = models.CharField(
        max_length=40, blank=True, null=True)
    region = models.CharField(
        max_length=40, blank=True, null=True)
    owner_name = models.CharField(
        max_length=60, blank=True, null=True)
    year_established = models.IntegerField(
        blank=True, null=True)
    year_closed = models.IntegerField(
        blank=True, null=True)
    year_demolished = models.IntegerField(
        blank=True, null=True)
    geolocation = LocationField(based_fields=['name'],
        blank=True, null=True)
    image_url = models.CharField(
        max_length=200, blank=True, null=True)
    logo_url = models.CharField(
        max_length=200, blank=True, null=True)
    owner = models.ForeignKey('Company',
        on_delete=models.SET_NULL, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Distilleries'

    def __str__(self):
       return self.name

    @property
    def latitude(self):
        return self.geolocation.x

    @property
    def longitude(self):
        return self.geolocation.y

    @property
    def coordinates(self):
        if self.geolocation:
            return format_coordinates(self.geolocation.x, self.geolocation.y)
        return '--'
    
    @property
    def image(self):
        if self.image_url:
            return self.image_url
        for scotch in Scotch.objects.filter(distillery=self):
            if scotch.image_url:
                return scotch.image_url
        return settings.PLACEHOLDER_IMAGE

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        # Get or create 
        if not self.owner and self.owner_name:
            company, _ = Company.objects.get_or_create(name=self.owner_name)
            self.owner = company
        return super().save(*args, **kwargs)

class Scotch(models.Model):
    name = models.CharField(
        max_length=100, unique=True, blank=True, null=True)
    # Just link Scotch to 750ml product from Virginia ABC if one exists
    distillery = models.ForeignKey('Distillery',
        on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Scotches'

    def __str__(self):
        return self.name

    def price(self):
        va_price_info = VirginiaPriceInfo.objects.get(scotch=self, size='750 ml')
        if va_price_info:
            return va_price_info.price
        return None
    price.short_description = 'Price'
    
    def description(self):
        va_price_info = VirginiaPriceInfo.objects.get(scotch=self, size='750 ml')
        if va_price_info:
            return va_price_info.description
        return None
    description.short_description = 'Description'

    @property
    def image_url(self):
        va_price_info = VirginiaPriceInfo.objects.filter(scotch=self)
        for info in va_price_info:
            if info.image_url:
                return info.image_url
        return None
    
    @property
    def style(self):
        va_price_info = VirginiaPriceInfo.objects.get(scotch=self, size='750 ml')
        if va_price_info:
            return va_price_info.hierarchy_detail
        return ''



# TODO make this a ManyToOne for Distillery (or individual whiskies?)
# class TasteProfile(models.Model):
#     pass
