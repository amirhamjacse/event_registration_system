   
from django.urls import path
from event_manager import views

urlpatterns = [
    path('list/', views.EventListView.as_view(),
         name='event_list'
        ),
    path('<int:event_id>/register/',
         views.RegisterEventView.as_view(),
         name='register_event'
        ),
    # path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
