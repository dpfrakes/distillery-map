from django.contrib import admin

from apps.entities.filters import PriceRangeFilter
from apps.entities.models import Company, Distillery, Scotch

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

admin.site.register(Company, CompanyAdmin)
admin.site.register(Distillery, DistilleryAdmin)
admin.site.register(Scotch, ScotchAdmin)
