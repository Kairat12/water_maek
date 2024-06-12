from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import *


# Create your views here.
@login_required
def index(request):
    rpv5 = RPV5.objects.latest('id')
    rpv6 = RPV6.objects.latest('id')
    rpv7 = RPV7.objects.latest('id')
    return render(request, 'main.html', {'rpv5': rpv5, 'rpv6': rpv6, 'rpv7': rpv7})
