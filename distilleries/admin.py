from django.contrib import admin


from distilleries.models import Distillery

class DistilleryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Distillery, DistilleryAdmin)