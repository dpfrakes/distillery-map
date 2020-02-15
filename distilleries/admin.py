from django.contrib import admin


from distilleries.models import Distillery

class DistilleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'region')
    list_filter = ('region',)
    ordering = ('name',)

admin.site.register(Distillery, DistilleryAdmin)
