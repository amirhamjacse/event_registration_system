from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from event_manager.models import Event, EventRegistration


class DashboardView(
    LoginRequiredMixin,
    UserPassesTestMixin, View
):
    template_name = 'dashboard.html'

    def test_func(self):
        return self.request.user.is_active

    def get(self, request):
        search_query = request.GET.get('search', '')

        query = EventRegistration.objects.filter(
            user=self.request.user,
            is_active=True
        )

        if search_query:
            query = query.filter(
                Q(event__title__icontains=search_query)|
                Q(event__location_name__icontains=search_query)
            )

        context = {
            'user_event': query,
            'search_query': search_query
        }
        return render(request, self.template_name, context)
