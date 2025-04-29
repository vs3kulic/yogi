import random
import os
import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from app.models import YogaClass  # Import the YogaClass model

logger = logging.getLogger(__name__)

def index(request):
    """
    Home page view that also resets the questionnaire session data.
    """
    # Reset questionnaire session data
    request.session.pop('shuffled_questions', None)
    request.session.pop('current_question_index', None)
    request.session.pop('responses', None)

    return render(request, 'index.html')

def info(request):
    """
    Render a placeholder lore/info page.
    """
    return render(request, 'info.html')

def questionnaire(request):
    """
    Handle the questionnaire logic.
    """
    if request.method == "POST":
        answer = request.POST.get("answer")
        if answer:
            responses = request.session.get('responses', [])
            responses.append(answer)
            request.session['responses'] = responses

        # Move to the next question or calculate the result
        current_question_index = request.session.get('current_question_index', 0)
        current_question_index += 1
        request.session['current_question_index'] = current_question_index

        if current_question_index >= len(questions):
            return redirect('calculate_result')  # Ensure this matches the name in urls.py

    # Render the current question
    question = questions[request.session.get('current_question_index', 0)]
    return render(request, 'questionnaire.html', {'question': question})

def reset_questionnaire(request):
    """
    Reset the questionnaire by clearing session data.
    """
    request.session.pop('shuffled_questions', None)
    request.session.pop('current_question_index', None)
    request.session.pop('responses', None)
    return redirect('index')  # Redirect to the home page or any other page

def calculate_result(request):
    """
    Calculate the user's yoga type based on their answers.
    """
    # Retrieve the user's responses from the session
    responses = request.session.get('responses', [])

    # Mapping of answers to result types
    answer_to_result_type = {
        "A": "Burnout-Yogini",
        "B": "Ashtanga-Warrior",
        "C": "Homeoffice-Yogini",
        "D": "Casual-Stretcher",
    }

    # Count the occurrences of each result type
    result_type_count = {}
    for response in responses:
        result_type = answer_to_result_type.get(response)
        if result_type:
            result_type_count[result_type] = result_type_count.get(result_type, 0) + 1

    # Determine the most frequent result type
    result_yoga_type = max(result_type_count, key=result_type_count.get, default="Unbekannt")

    # Store the result type in the session
    request.session['result_type'] = result_yoga_type

    # Pass the result to the template
    return render(request, 'result.html', {
        'result_text': f"Dein Yoga-Typ ist: <strong>{result_yoga_type}</strong>!",
        'result_type': result_yoga_type
    })

def recommended_classes(request):
    """
    Display recommended classes based on the user's result type.
    """
    # Get the user's result type from the session
    result_type = request.session.get('result_type', None)

    # Fetch classes from the database based on the result type
    filtered_classes = YogaClass.objects.filter(yoga_type=result_type)  # Use 'yoga_type' instead of 'type'

    return render(request, 'recommended_classes.html', {'classes': filtered_classes, 'result_type': result_type})

# Define the questions for the questionnaire
questions = [
    {
        "number": 1,
        "question": "Wie fühlt sich dein Körper aktuell an?",
        "answers": {
            "A": "Ich bin basically der Typ flexible Brezel – super elastisch in allen Positionen.",
            "B": "Ganz solide, aber manchmal knarre ich beim Aufstehen wie ein Holzstuhl.",
            "C": "Mein Körper ist ein work in progress – ich bin da realistisch.",
            "D": "Bewegung gibt’s bei mir meistens nur dann wenn es unbedingt sein muss."
        }
    },
    {
        "number": 2,
        "question": "Wie läuft’s bei dir mit Verletzungen oder Einschränkungen?",
        "answers": {
            "A": "Momentan hab ich keine akuten oder chronischen Verletzungen.",
            "B": "Ich komme mit Altlasten – meine Schulter erzählt noch vom Festival ’18.",
            "C": "Mein Körper kommt mir derzeit wie eine chronische Baustelle vor.",
            "D": "Ich bin aktuell völlig out of order — aber ich will zurück ins Game."
        }
    },
    {
        "number": 3,
        "question": "Dein Commitment-Level zu Yoga?",
        "answers": {
            "A": "Situationship-Yogi. Ich und Yoga waren immer schon on-off.",
            "B": "Yoga war Liebe auf den ersten Blick. Ich bin vollkommen committed!",
            "C": "YouTube-Yoga und ich haben eine intensive Fernbeziehung.",
            "D": "Ich schau mal. Ich hab gehört es gibt Snacks und Tee nach der Klasse."
        }
    },
    {
        "number": 4,
        "question": "Welche Vibes spürst du, wenn du an Yoga denkst?",
        "answers": {
            "A": "Faszien-Liebe: Entkrampfen, durchatmen, alles loslassen – pls massage my soul.",
            "B": "Power-Mover: Ich brauch Action! Schwitzen, stretchen, strong AF werden.",
            "C": "Slow-Flow: Ich will flowen und chillen.",
            "D": "Zen-Seeker: Ich weiß ich brauche mehr im Leben — vielleicht ist es Yoga."
        }
    },
    {
        "number": 5,
        "question": "Wie willst du dein Yoga erleben?",
        "answers": {
            "A": "Kollektiver Vibe like a Sunday Brunch – nur mit Asanas.",
            "B": "Mat Queen: Ich bleibe auf meiner Matte, alles andere um mich herum blende ich aus.",
            "C": "Zen-Master: Hauptsache gemütlich. Langsamer, tiefer, länger.",
            "D": "Ich brauch klare Ansagen – step by step, sonst verlauf ich mich."
        }
    },
]