# events/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.views import View
from event_manager.models import Event, EventRegistration
from event_manager.forms import EventForm, RegistrationForm


class EventListView(
    LoginRequiredMixin, View,
    UserPassesTestMixin
):
    template_name = 'events/event_list.html'

    def test_func(self):
        return self.request.user.is_active

    def get(self, request):
        events = Event.objects.all()
        return render(
            request, self.template_name, {'events': events}
        )


class RegisterEventView(
    LoginRequiredMixin, UserPassesTestMixin, View,
):
    template_name = 'events/register_event.html'

    def test_func(self):
        return self.request.user.is_active

    def get(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        form = RegistrationForm(initial={'event': event})
        return render(
            request, self.template_name, {'event': event, 'form': form}
        )

    def post(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        form = RegistrationForm(request.POST)

        if form.is_valid():
            if event.available_slots > 0:
                EventRegistration.objects.create(
                    event=event, user=request.user
                )
                event.available_slots -= 1
                event.save()
                messages.success(
                    request, 'Successfully registered for the event.'
                )
                return redirect('event_list')
            else:
                messages.error(
                    request, 'No available slots for this event.'
                )
        else:
            messages.error(request, 'Invalid form submission.')

        return render(
            request, self.template_name, {'event': event, 'form': form}
        )
