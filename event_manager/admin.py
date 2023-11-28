from django.contrib import admin
from event_manager import models
# Register your models here.


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


@admin.register(models.EventRegistration)
class EventRegistrationModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'event',
        'user',
        'registration_date',
    ]
