from django.shortcuts import render, redirect
from .game import Game

def index(request):
    game = Game()
    heroes = [character.name for character in game.main_characters]
    return render(request, 'index.html', {'heroes': heroes})

def select_character(request):
    if request.method == 'POST':
        character_number = int(request.POST.get('character_number'))
        game = Game()
        selected_hero = game.select_character(character_number)
        if selected_hero:
            request.session['selected_hero'] = selected_hero.name
            message = f"You picked {selected_hero.name} as your fighter!"
            return render(request, 'select_character.html', {'message': message})
        else:
            message = "Invalid choice. Please try again."
            return render(request, 'index.html', {'message': message})
    return redirect('index')

def opponent_selected(request):
    game = Game()
    selected_hero_name = request.session.get('selected_hero')
    opponent = game.select_opponent()
    request.session['opponent'] = opponent.name
    message = f"You picked {selected_hero_name} as your fighter! Your opponent is {opponent.name}."
    return render(request, 'opponent_selected.html', {'message': message})

def coin_toss(request):
    if request.method == 'POST':
        user_choice = request.POST.get('coin_choice')
        game = Game()
        coin_result = game.coin_toss(user_choice)
        return render(request, 'coin_toss_result.html', {'coin_result': coin_result})
    return render(request, 'coin_toss.html')

def battle(request):
    game = Game()
    selected_hero_name = request.session.get('selected_hero')
    opponent_name = request.session.get('opponent')
    player = next(character for character in game.main_characters if character.name == selected_hero_name)
    opponent = next(character for character in game.antagonists if character.name == opponent_name)
    scores = game.run_round(player, opponent)
    result = game.declare_winner(scores)
    steps = scores[2]
    return render(request, 'battle.html', {'result': result, 'steps': steps})