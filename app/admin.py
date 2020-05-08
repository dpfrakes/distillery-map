from django.contrib import admin

from app.filters import PriceRangeFilter
from app.models import Distillery, Scotch, ABCInfo

class DistilleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'region', 'coordinates',)
    list_filter = ('region',)
    ordering = ('name',)

class ScotchAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'distillery',)
    readonly_fields = ('price', 'description', )
    list_filter = (PriceRangeFilter, )
    ordering = ('name',)

class ABCInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'price', 'sku',)
    list_filter = ('size', PriceRangeFilter,)
    ordering = ('name',)

admin.site.register(Distillery, DistilleryAdmin)
admin.site.register(Scotch, ScotchAdmin)
admin.site.register(ABCInfo, ABCInfoAdmin)
