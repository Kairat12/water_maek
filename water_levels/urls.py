from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.urls import path

from .views import *

app_name = 'water_levels'

urlpatterns = [
    path('', index, name='index'),
    path('graphs/', graphs, name='graphs'),
    path('upload_data/', upload_data, name='upload_data'),
]