from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .models import Character, BattleOutcome
from .game import Game, GameCharacter  # Import the necessary classes and functions
import random

def index(request):
    heroes = Character.objects.filter(is_main_character=True)
    return render(request, 'index.html', {'heroes': heroes})

def select_character(request):
    if request.method == 'POST':
        character_id = request.POST.get('character_id')
        if not character_id:
            message = "No character selected. Please try again."
            return render(request, 'index.html', {'message': message, 'heroes': Character.objects.filter(is_main_character=True)})

        character_id = int(character_id)
        try:
            selected_hero = Character.objects.get(id=character_id)
        except ObjectDoesNotExist:
            return HttpResponse("Selected hero not found.", status=404)

        request.session['selected_hero'] = selected_hero.name
        message = f"You picked {selected_hero.name} as your fighter!"
        return render(request, 'select_character.html', {'message': message})
    return redirect('index')

def opponent_selected(request):

    opponent = Character.objects.filter(is_antagonist=True).order_by('?').first()
    if not opponent:
        return HttpResponse("No opponent found.", status=404)

    request.session['opponent'] = opponent.name
    message = f"Your opponent is {opponent.name}!"
    return render(request, 'opponent_selected.html', {'message': message})

def coin_toss(request):
    if request.method == 'POST':
        user_choice = request.POST.get('coin_choice')
        coin_result = "Heads" if random.choice([True, False]) else "Tails"
        return render(request, 'coin_toss_result.html', {'coin_result': coin_result})
    return render(request, 'coin_toss.html')

def battle(request):
    selected_hero_name = request.session.get('selected_hero')
    opponent_name = request.session.get('opponent')

    try:
        player = Character.objects.get(name=selected_hero_name)
    except ObjectDoesNotExist:
        return HttpResponse("Selected hero not found.", status=404)

    try:
        opponent = Character.objects.get(name=opponent_name)
    except ObjectDoesNotExist:
        return HttpResponse("Opponent not found.", status=404)

    # Create game characters
    player_character = GameCharacter(player.name, 100, 10)  # Example life points and attack points
    opponent_character = GameCharacter(opponent.name, 100, 10)  # Example life points and attack points

    # Simulate the battle
    game = Game()
    player_life, opponent_life, steps = game.run_round(player_character, opponent_character)
    result = "Win" if player_life > 0 else "Lose"

    # Save the battle outcome to the database
    BattleOutcome.objects.create(
        player=selected_hero_name,
        opponent=opponent_name,
        outcome=result
    )

    return render(request, 'battle.html', {'result': result, 'steps': steps})

def battle_results(request):
    selected_hero_name = request.session.get('selected_hero')
    outcomes = BattleOutcome.objects.filter(player=selected_hero_name).order_by('-timestamp')
    return render(request, 'battle_results.html', {'character_name': selected_hero_name, 'outcomes': outcomes})