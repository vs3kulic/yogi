from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .game_logic.game import Game

def index(request):
    return render(request, 'game/index.html')

def play_game(request):
    return render(request, 'game/play.html')

@api_view(['POST'])
def select_character(request):
    game = Game()
    character_id = request.data.get('character_id')
    character = game.select_character(character_id)
    return Response({'character': character})

@api_view(['GET'])
def select_opponent(request):
    game = Game()
    opponent = game.select_opponent()
    return Response({'opponent': opponent})

@api_view(['POST'])
def run_round(request):
    game = Game()
    player = request.data.get('player')
    opponent = request.data.get('opponent')
    result = game.run_round(player, opponent)
    winner = game.declare_winner(result)
    return Response({
        'result': result,
        'winner': winner
    })