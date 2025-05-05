from django.shortcuts import render
from .utils import recommend_artifact
from app.models import Character, Artifact

def artifact_recommendation_view(request):
    character_id = request.session.get('selected_character_id')
    opponent_id = request.session.get('opponent_id')
    coin_toss_result = request.session.get('coin_toss_result')

    character = Character.objects.get(id=character_id)
    opponent = Character.objects.get(id=opponent_id)
    artifacts = Artifact.objects.filter(character=character)

    recommendations = []
    for artifact in artifacts:
        probability = recommend_artifact(character, opponent, artifact, coin_toss_result)
        recommendations.append((artifact, probability))

    # Sort artifacts by probability of winning
    recommendations.sort(key=lambda x: x[1], reverse=True)
    best_artifact = recommendations[0][0] if recommendations else None

    return render(request, 'artifact_selection.html', {
        'character': character,
        'artifacts': artifacts,
        'best_artifact': best_artifact,
        'recommendations': recommendations
    })
