from django.urls import path
from . import views

app_name="playlist"

urlpatterns = [
    path('', views.home, name='home'),
    path('track/<int:pk>', views.track_details, name='track-detail'),
 
]
