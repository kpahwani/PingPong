from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from players.serializer import PlayersSerializer
from .models import Championships
from players.models import Players
# Create your views here.


def index(request):
    return render(request, 'referee/index.html', context={'c_list':Championships.get_championships_list()})


@api_view(['GET'])
def start_game(request):
    c_ship = Championships.objects.create()
    winner = c_ship.start_championship()
    if winner:
        serializer = PlayersSerializer(winner)
        return render(request, 'referee/index.html', {'data': '{} user won the game'.format(serializer.data['username'])},
                      status=status.HTTP_200_OK)
    else:
        return render(request, 'referee/index.html', {'data': 'Minimum 8 players required'}, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_active_players(request):
    players = Players.objects.filter(is_active=True)
    serializer = PlayersSerializer(players, many=True)
    return render(request, 'referee/index.html', {'data': 'Total {} users active'.format(len(serializer.data))},
                  status=status.HTTP_200_OK)


@api_view(['GET'])
def set_all_user_active(request):
    Players.objects.update(is_active=True)
    return render(request, 'referee/index.html', {'data': 'All user are active'},
                  status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def get_results(request):
    if request.method == 'POST':
        details = Championships.get_championship_details(request.POST['item_id'])
        return render(request, 'referee/index.html', {'details': details},
                      status=status.HTTP_200_OK)
    else:
        return render(request, 'referee/index.html', status=status.HTTP_400_BAD_REQUEST)