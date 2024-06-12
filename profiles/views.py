from django.contrib.auth.models import User
from django.shortcuts import render




def user_info(request):
    user_profile = User.objects.get(username=request.user)
    return render(request, 'profiles/profile.html', {'user_info': user_profile})
