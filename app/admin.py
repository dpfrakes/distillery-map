from django.contrib import admin

from app.filters import PriceRangeFilter
from app.models import Company, Distillery, Scotch, ABCInfo

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'flag',)
    readonly_fields = ('owned_properties', )
    # list_filter = ('country',)
    ordering = ('name',)

class DistilleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'location', 'region', 'coordinates',)
    exclude = ('slug',)
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

admin.site.register(Company, CompanyAdmin)
admin.site.register(Distillery, DistilleryAdmin)
admin.site.register(Scotch, ScotchAdmin)
admin.site.register(ABCInfo, ABCInfoAdmin)
