# events/forms.py
from django import forms
from event_manager.models import Event, EventRegistration


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'title',
            'description',
            'date',
            'time',
            'location_name',
            'available_slots'
        ]

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = ['event']

