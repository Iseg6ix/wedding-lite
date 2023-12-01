from django.shortcuts import render
from django.http import JsonResponse
from .models import Bride, Groom


def couple(request):
    bride_data = {
        'firstname': 'Silva',
        'lastname': 'Robbison',
        'age': 28,
        'bridesmaid': 'Clara',
    }
    groom_data = {
        'firstname': 'Troy',
        'lastname': 'Jackson',
        'age': 30,
        'bestman': 'Sniper',
    }
    
    data = {
        'bride': bride_data,
        'groom': groom_data,
    }
    return JsonResponse(data, safe=False)


