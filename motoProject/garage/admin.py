

from django.contrib import admin

from .models import Motorcycle

class MotorcycleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['motorcycle_text']}),
        ('Brand', {'fields': ['motorcycle_brand']}),
        ('Description', {'fields': ['motorcycle_description']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Motorcycle, MotorcycleAdmin)
