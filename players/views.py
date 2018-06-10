from django.shortcuts import render
from .models import Players
# Create your views here.


def index(request):
    return render(request, 'players/index.html')


def create_player(request):
    if request.method == 'POST':
        player = request.POST
        if not Players.objects.filter(username=player['username']).exists():
            Players.objects.create(username=player['username'], password=player['password'])
            return render(request, 'players/index.html', context={'message': 'Player added'})
        else:
            return render(request, 'players/create_player.html', context={'message': 'Player already exist'})
    else:
        return render(request, 'players/create_player.html')


def join_game(request):
    if request.method == 'POST':
        player = request.POST
        if Players.objects.filter(username=player['username'], password=player['password']).exists():
            Players.objects.select_for_update().filter(username=player['username']).update(array_length=player['array_length'], is_active=True)
            return render(request, 'players/index.html', context={'message': 'Player added to the game'})
        return render(request, 'players/join_game.html', context={'message': 'Invalid user details'})
    else:
        return render(request, 'players/join_game.html')

