from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin
)
from django.views import View
from django.shortcuts import render, redirect


class HomeView(LoginRequiredMixin,
    UserPassesTestMixin, View
):
    template_name = 'home.html'

    def test_func(self):
        return self.request.user.is_active

    def get(self, request):
        return render(request, self.template_name)
