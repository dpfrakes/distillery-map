from django.conf import settings
from django.contrib.gis.geos import Point
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.text import slugify

from django_countries.fields import CountryField
from location_field.models.spatial import LocationField

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
            distillery_list = [f'<a href="{reverse("admin:app_distillery_change", args=[d.pk])}">{d.name}</a>' for d in distilleries]
            return format_html('<br/>'.join(distillery_list))
        except Exception as e:
            print(e)
            return None
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
    # Just link Scotch to 750ml product from ABC if one exists
    distillery = models.ForeignKey('Distillery',
        on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Scotches'

    def __str__(self):
        return self.name

    def price(self):
        abc_info = ABCInfo.objects.get(scotch=self, size='750 ml')
        if abc_info:
            return abc_info.price
        return None
    price.short_description = 'Price'
    
    def description(self):
        abc_info = ABCInfo.objects.get(scotch=self, size='750 ml')
        if abc_info:
            return abc_info.description
        return None
    description.short_description = 'Description'

    @property
    def image_url(self):
        abc_data = ABCInfo.objects.filter(scotch=self)
        for info in abc_data:
            if info.image_url:
                return info.image_url
        return None
    
    @property
    def style(self):
        abc_info = ABCInfo.objects.get(scotch=self, size='750 ml')
        if abc_info:
            return abc_info.hierarchy_detail
        return ''

class ABCInfo(models.Model):
    """
    Information specific to ABC stores, separated from Scotches
    for price info, hierarchy, etc. all specific to Virginia ABC
    """
    sku = models.CharField(
        max_length=200, unique=True)
    unique_id = models.CharField(
        max_length=30, help_text='Unique to product but not size/price')
    name = models.CharField(
        max_length=100)
    description = models.CharField(
        max_length=200, blank=True, null=True)
    size = models.CharField(
        max_length=20)
    price = models.DecimalField(
        max_digits=9, decimal_places=2, blank=True, null=True)
    product_uri = models.URLField(
        blank=True, null=True)
    hierarchy_division = models.CharField(
        max_length=50, blank=True, null=True) # Alcohol
    hierarchy_class = models.CharField(
        max_length=50, blank=True, null=True) # Spirits
    hierarchy_category = models.CharField(
        max_length=50, blank=True, null=True) # Whiskey
    hierarchy_type = models.CharField(
        max_length=50, blank=True, null=True) # Scotch
    hierarchy_detail = models.CharField(
        max_length=50, blank=True, null=True) # Blended/Single Malt
    hierarchy_fact = models.CharField(
        max_length=50, blank=True, null=True) # Highland/Speyside/Other
    hierarchy_imported = models.CharField(
        max_length=50, blank=True, null=True) # 1
    hierarchy_flavored = models.CharField(
        max_length=50, blank=True, null=True) # 0
    hierarchy_vap = models.CharField(
        max_length=50, blank=True, null=True) # 0
    image_url = models.URLField(
        blank=True, null=True)
    scotch = models.ForeignKey('Scotch',
        on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'ABC Info'
        # unique_together = ('name', 'size',)

    def __str__(self):
        return f'{self.name} ({self.size})'

# TODO make this a ManyToOne for Distillery (or individual whiskies?)
# class TasteProfile(models.Model):
#     pass
