# filepath: /Users/vajosekulic/Documents/Programming/Fellowships/Fellowships/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .game import Game

def index(request):
    game = Game()
    heroes = [character.name for character in game.main_characters]
    return render(request, 'index.html', {'heroes': heroes})

def select_character(request):
    if request.method == 'POST':
        character_number = int(request.POST.get('character_number')) - 1
        game = Game()
        selected_hero = game.select_character(character_number)
        if selected_hero:
            return HttpResponse(f"You picked {selected_hero.name} as your fighter!")
        else:
            return HttpResponse("Invalid choice. Please try again.")
    return redirect('index')