from django.db import models


class VirginiaPriceInfo(models.Model):
    """
    Information specific to Virginia ABC stores, separated from Scotches
    for price info, hierarchy, etc. all specific to Virginia ABC
    """
    sku = models.CharField(
        max_length=200, unique=True)
    unique_id = models.CharField(
        max_length=100, help_text='Unique to product but not size/price')
    name = models.CharField(
        max_length=100)
    scotch = models.ForeignKey('entities.Scotch',
        on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(
        max_length=500, blank=True, null=True)
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

    class Meta:
        verbose_name = 'Virginia price info'
        verbose_name_plural = 'Virginia'
        # unique_together = ('name', 'size',)

    def __str__(self):
        return f'{self.scotch.name} ({self.size})'
