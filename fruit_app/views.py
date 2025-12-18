from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

# Create your views here.


def send_fruits_view(request):
    fruits = [
        {"name": "Apple", "weight": 150, "color": "red"},
        {"name": "Banana", "weight": 120, "color": "yellow"},
        {"name": "Cherry", "weight": 10, "color": "red"},
        {"name": "Date", "weight": 7, "color": "brown"},
        {"name": "Elderberry", "weight": 5, "color": "black"},
    ]
    return JsonResponse(fruits, safe=False)