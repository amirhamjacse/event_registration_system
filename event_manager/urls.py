   
from django.urls import path
from event_manager import views

urlpatterns = [
    path('create/',
         views.EventCreateView.as_view(),
         name='event_create'
        ),
    path('list/', views.EventListView.as_view(),
         name='event_list'
        ),
    path('<int:event_id>/register/',
         views.RegisterEventView.as_view(),
         name='register_event'
        ),
    path('<int:event_id>/unregister/',
         views.UnregisterEventView.as_view(),
         name='unregister_event'
        ),
    path('<int:pk>/details/',
         views.EventDetailsView.as_view(),
         name='events_details'
        ),
]
