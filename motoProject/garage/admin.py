

from django.contrib import admin

from .models import Motorcycle, Description

class MotorcycleAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['motorcycle_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class DescriptionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['motorcycle']}),
        ('Description', {'fields': ['description_text']}),
        ('Likes', {'fields': ['likes']}),
    ]

admin.site.register(Motorcycle, MotorcycleAdmin)
admin.site.register(Description, DescriptionAdmin)
