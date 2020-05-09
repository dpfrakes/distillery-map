from django.contrib import admin

from apps.entities.filters import PriceRangeFilter
from apps.pricing.models import VirginiaPriceInfo

class VirginiaPriceInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'scotch', 'size', 'price', 'sku',)
    list_filter = ('size', PriceRangeFilter,)
    ordering = ('name',)

admin.site.register(VirginiaPriceInfo, VirginiaPriceInfoAdmin)
