# Inside maps/views.py

from django.shortcuts import render
from .models import Location

def map_view(request):
    locations = Location.objects.all()
    return render(request, 'maps/map.html', {'locations': locations})

