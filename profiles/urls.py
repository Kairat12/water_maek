from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.urls import path

app_name = 'profiles'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('logout/', LogoutView.as_view(), name='logout'),
]