from django.contrib import admin
from . import models


@admin.register(models.Event)
class EventModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'date',
        'time',
        'location_name',
        'available_slots',
    ]
    
    search_fields = ['title', 'description', 'location_name']
    list_filter = ['date', 'time', 'available_slots']
    list_display_links = ['title']
    list_editable = ['available_slots']
    list_per_page = 10
    date_hierarchy = 'date'
    ordering = ['date']
    readonly_fields = ['id']


@admin.register(models.EventRegistration)
class EventRegistrationModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'event',
        'user',
        'registration_date',
    ]

    search_fields = ['event__title', 'user__username']
    list_filter = ['event', 'registration_date']
