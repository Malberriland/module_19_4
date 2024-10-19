from django.shortcuts import render
from .models import *


# Create your views here.
def platform(request):
    return render(request, 'fourth_task/platform.html')

def game(request):
    games = Game.objects.all()
    context = {
        'games': games
    }
    return render(request, 'fourth_task/games.html', context)

def cart(request):
    return render(request, 'fourth_task/cart.html')
