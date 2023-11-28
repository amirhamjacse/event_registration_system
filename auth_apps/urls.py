from django.urls import path
from auth_apps import views

urlpatterns = [

    path('register/',
         views.RegistrationView.as_view(),
         name='register'
         ),
    path('accounts/login/',
         views.LoginView.as_view(),
         name='login'
         ),
    path('accounts/logout/',
         views.LogoutView.as_view(),
         name='logout'
         ),
]
