# Inside maps/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='map-view'),
    # Define other URL patterns as needed
]
