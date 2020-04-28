from django.contrib import admin

from app.models import Distillery

class DistilleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'region', 'coordinates',)
    list_filter = ('region',)
    ordering = ('name',)

admin.site.register(Distillery, DistilleryAdmin)
