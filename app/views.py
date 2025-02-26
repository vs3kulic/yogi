import random
from django.shortcuts import render, get_object_or_404, redirect
from .models import Character, BattleOutcome, Artifact

def index(request):
    """
    Render the index page.
    """
    return render(request, 'index.html')

def character_selection(request):
    """
    Display a list of main characters so the user can choose one.
    """
    characters = Character.objects.filter(is_main_character=True)
    return render(request, 'character_selection.html', {'characters': characters})

def select_character(request, character_id):
    """
    Select a character, assign quotes if applicable, and store its ID in the session.
    """
    character = get_object_or_404(Character, id=character_id)
    character.life_points = 100
    character.save()
    
    if character.is_main_character:
        character.fetch_and_assign_quotes()  # Fetch and assign quotes only for main characters
    request.session['selected_character_id'] = character.id  # Store the selected character's ID in the session
    return render(request, 'select_character.html', {'character': character})

def opponent_selected(request):
    opponent = Character.objects.filter(is_antagonist=True).order_by('?').first()
    request.session['opponent_id'] = opponent.id
    message = "You have selected an opponent."
    return render(request, 'opponent_selected.html', {'character': opponent, 'message': message})

def coin_toss(request):
    if request.method == 'POST':
        user_choice = request.POST.get('coin_choice')
        coin_result = random.choice(['heads', 'tails'])
        result = 'win' if user_choice == coin_result else 'lose'
        return redirect('coin_toss_result', result=result)
    return render(request, 'coin_toss.html')

def coin_toss_result(request, result):
    request.session['coin_toss_result'] = result
    return render(request, 'coin_toss_result.html', {'result': result})

def battle(request):
    selected_character_id = request.session.get('selected_character_id')
    opponent_id = request.session.get('opponent_id')
    main_character = get_object_or_404(Character, id=selected_character_id)
    opponent = get_object_or_404(Character, id=opponent_id)
    
    # Reset life points for testing
    main_character.life_points = 100
    opponent.life_points = 100
    main_character.save()
    opponent.save()

    coin_toss_result = request.session.get('coin_toss_result')
    print("Coin toss result:", coin_toss_result)
    
    steps = []
    first_attacker = main_character if coin_toss_result == 'win' else opponent
    second_attacker = opponent if first_attacker == main_character else main_character

    while main_character.life_points > 0 and opponent.life_points > 0:
        damage = first_attacker.attack(second_attacker)
        steps.append(f"{first_attacker.name} attacks {second_attacker.name} and deals {damage} damage.")
        if second_attacker.life_points <= 0:
            steps.append(f"{second_attacker.name} is defeated!")
            outcome = 'Win' if first_attacker == main_character else 'Loss'
            main_artifact_id = request.session.get('main_artifact_id')
            opponent_artifact_id = request.session.get('opponent_artifact_id')

            BattleOutcome.objects.create(
                player=main_character.name,
                opponent=opponent.name,
                outcome=outcome,
                main_artifact=Artifact.objects.get(id=main_artifact_id) if main_artifact_id else None,
                opponent_artifact=Artifact.objects.get(id=opponent_artifact_id) if opponent_artifact_id else None,
            )
            break

        damage = second_attacker.attack(first_attacker)
        steps.append(f"{second_attacker.name} attacks {first_attacker.name} and deals {damage} damage.")
        if first_attacker.life_points <= 0:
            steps.append(f"{first_attacker.name} is defeated!")
            outcome = 'Loss' if first_attacker == main_character else 'Win'
            main_artifact_id = request.session.get('main_artifact_id')
            opponent_artifact_id = request.session.get('opponent_artifact_id')

            BattleOutcome.objects.create(
                player=main_character.name,
                opponent=opponent.name,
                outcome=outcome,
                main_artifact=Artifact.objects.get(id=main_artifact_id) if main_artifact_id else None,
                opponent_artifact=Artifact.objects.get(id=opponent_artifact_id) if opponent_artifact_id else None,
            )
            break

    return render(request, 'battle.html', {'steps': steps})

def battle_results(request):
    selected_character_id = request.session.get('selected_character_id')
    character = get_object_or_404(Character, id=selected_character_id)
    outcomes = BattleOutcome.objects.filter(player=character).order_by('-timestamp')
    
    return render(request, 'battle_results.html', {
        'character_name': character.name,
        'outcomes': outcomes
    })

def artifact_selection(request):
    selected_character_id = request.session.get('selected_character_id')
    main_character = get_object_or_404(Character, id=selected_character_id)
    if not main_character:
        return redirect('index')
    artifacts = Artifact.objects.filter(character=main_character)
    return render(request, 'artifact_selection.html', {
        'character': main_character,
        'artifacts': artifacts,
    })

def artifact_selected(request):
    if request.method == 'POST':
        artifact_id = request.POST.get('artifact_id')
        if not artifact_id:
            selected_character_id = request.session.get('selected_character_id')
            main_character = get_object_or_404(Character, id=selected_character_id)
            artifacts = Artifact.objects.filter(character=main_character)
            error = "Please select an artifact before continuing."
            return render(request, 'artifact_selection.html', {
                'character': main_character,
                'artifacts': artifacts,
                'error': error,
            })

        selected_character_id = request.session.get('selected_character_id')
        main_character = get_object_or_404(Character, id=selected_character_id)
        artifact = get_object_or_404(Artifact, pk=artifact_id)
        request.session['main_artifact_id'] = artifact.id
        return redirect('opponent_selected')

def opponent_artifact(request):
    opponent_id = request.session.get('opponent_id')
    if not opponent_id:
        return redirect('index')
    opponent = get_object_or_404(Character, id=opponent_id)
    artifacts = list(Artifact.objects.filter(character=opponent))
    selected_artifact = random.choice(artifacts) if artifacts else None
    request.session['opponent_artifact_id'] = selected_artifact.id
    return render(request, 'opponent_artifact.html', {
        'opponent': opponent,
        'selected_artifact': selected_artifact,
    })

def lore(request):
    """
    Render a placeholder lore/info page.
    """
    return render(request, 'lore.html')

def prepare_battle(request):
    # Fetch your character and opponent objects using session variables or URL parameters
    character = get_object_or_404(Character, pk=request.session.get('character_id'))
    opponent = get_object_or_404(Character, pk=request.session.get('opponent_id'))
    
    # Reset life_points for both to 100
    character.life_points = 100
    opponent.life_points = 100
    character.save()
    opponent.save()
    
    # Now proceed with the battle or redirect to the battle view/template
    return redirect('battle')
