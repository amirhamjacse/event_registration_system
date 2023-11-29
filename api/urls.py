from django.urls import path
from .views import(
    EventListView, EventDetailsView,
    UserEventRegistrationView, UserRegisteredEventsView
)


urlpatterns = [
    path('events/',
         EventListView.as_view(),
         name='event-list'
        ),
    path('events/<int:pk>/details/',
         EventDetailsView.as_view(),
        name='event-details'
        ),
    path('events/<int:event_id>/register/',
         UserEventRegistrationView.as_view(),
         name='user-event-register'
        ),
    path('events/registered/',
         UserRegisteredEventsView.as_view(),
         name='user-registered-events'
        ),
]
