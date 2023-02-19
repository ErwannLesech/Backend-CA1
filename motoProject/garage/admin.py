

from django.contrib import admin

from .models import Motorcycle, Description

class MotorcycleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['motorcycle_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Motorcycle, MotorcycleAdmin)

