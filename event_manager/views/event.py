# events/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.contrib import messages
from django.views import View
from django.views.generic import DetailView, CreateView
from django.db.models import Q
from event_manager.models import Event, EventRegistration
from event_manager.forms import (
    EventForm, RegistrationForm, UnregistrationForm
)


class EventCreateView(View):
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('event_list') 

    def get(self, request, *args, **kwargs):
        form = EventForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = EventForm(request.POST)
        print(form)
        if form.is_valid():
            event = form.save()
            print('save')
            return redirect(self.success_url)
        print('not')
        return render(request, self.template_name, {'form': form})


class EventListView(
    LoginRequiredMixin, View,
    UserPassesTestMixin
):
    template_name = 'events/event_list.html'

    def test_func(self):
        return self.request.user.is_active

    def get(self, request):
        search_query = request.GET.get('search', '')

        query = Event.objects.filter(
            is_active=True
        )

        if search_query:
            query = query.filter(
                Q(title__icontains=search_query)|
                Q(location_name__icontains=search_query)
            )

        context = {
            'events': query,
            'search_query': search_query
        }
        return render(
            request, self.template_name, context
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


class UnregisterEventView(
    LoginRequiredMixin, UserPassesTestMixin, View
):
    template_name = 'events/unregister_event.html'

    def test_func(self):
        return self.request.user.is_active

    def get(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        user_registration = EventRegistration.objects.filter(
            event=event, user=request.user
        ).first()

        if user_registration:
            form = UnregistrationForm(initial={'event': event})
            return render(
                request, self.template_name, {'event': event, 'form': form}
            )
        else:
            messages.error(
                request, 'You are not registered for this event.'
            )
            return redirect('event_list')

    def post(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        user_registration = EventRegistration.objects.filter(
            event=event, user=request.user
        ).first()

        if user_registration:
            # Unregister the user from the event
            user_registration.delete()
            event.available_slots += 1
            event.save()
            messages.success(
                request, 'Successfully unregistered from the event.'
            )
            return redirect('dashboard')
        else:
            messages.error(
                request, 'You are not registered for this event.'
            )

        return render(
            request, self.template_name, {'event': event, 'form': form}
        )


class EventDetailsView(
    LoginRequiredMixin, UserPassesTestMixin, DetailView
):
    model = Event
    template_name = 'events/event_details.html'
    context_object_name = 'event'

    def test_func(self):
        return self.request.user.is_active
