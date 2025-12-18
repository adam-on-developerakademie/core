from django.urls import path
from .views import send_fruits_view

urlpatterns = [
    path('', send_fruits_view, name='send_fruits'),
]