from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.urls import path

from .views import index

app_name = 'water_levels'

urlpatterns = [
    path('', index, name='index'),
]