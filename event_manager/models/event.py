# events/models.py
from django.db import models
from django.contrib.auth.models import User
from auth_apps.models import CustomUser
from event_registration_system.abstract_model import AbstractTimeMixin
from django.utils.translation import gettext_lazy as _


class Event(AbstractTimeMixin):
    title = models.CharField(
        _('Event Title'),
        max_length=255
    )
    description = models.TextField(
        _('Event Description'),
        blank=True, null=True
    )
    date = models.DateField(
        _('Event Date'),
        blank=True, null=True
    )
    time = models.TimeField(
        _('Event Time'),
        blank=True, null=True
    )
    location_name = models.CharField(
        _('Location Of Event'),
        max_length=255
    )
    available_slots = models.PositiveIntegerField(
        _('Available Slots')
    )

    def __str__(self):
        return f"{self.title}"


class EventRegistration(AbstractTimeMixin):
    event = models.ForeignKey(Event,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(CustomUser, 
        on_delete=models.CASCADE
    )
    registration_date = models.DateTimeField(
        _('Registration Date'), auto_now_add=True
    )

    def __str__(self) -> str:
        return f"{self.event}"
