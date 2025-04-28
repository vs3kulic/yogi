import random
import os
import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from dotenv import load_dotenv
from ml.utils import recommend_artifact  # Update this line
from .models import Character, BattleOutcome, Artifact

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
    questions = [
        {
            "id": 1,
            "question": "Wie fühlt sich dein Körper aktuell an?",
            "answers": {
                "A": "Basically eine menschliche Brezel – elastisch, aber vielleicht auch ein bisschen zerknittert.",
                "B": "Solide, aber mein Körper knarrt beim Aufstehen wie ein alter Holzstuhl.",
                "C": "Work in progress – ich bin da realistisch.",
                "D": "Team Kartoffel: Bewegung gibt’s bei mir primär zwischen Sofa und Kühlschrank."
            }
        },
        {
            "id": 2,
            "question": "Wie läuft’s bei dir mit Verletzungen oder Einschränkungen?",
            "answers": {
                "A": "Momentan frei wie ein Vogel!",
                "B": "Altlasten – meine Schulter erzählt noch vom Festival '18.",
                "C": "Chronisch? Leider ja, aber ich gebe meinem Körper Liebe.",
                "D": "Akut angeschlagen, aber ich will zurück ins Game!"
            }
        },
        {
            "id": 3,
            "question": "Dein Committment-Level zu Yoga?",
            "answers": {
                "A": "Ich und Yoga? It's giving Situationship – mal heiß, mal ghosting.",
                "B": "Ich will serious gehen – Commitment, Baby, let’s GOOOO.",
                "C": "YouTube und ich haben eine intensive Fernbeziehung.",
                "D": "Nur wenn’s gratis Snacks nach der Stunde gibt."
            }
        },
        {
            "id": 4,
            "question": "Wo spürst du am meisten Vibes, wenn du an Yoga denkst?",
            "answers": {
                "A": "Entkrampfen, durchatmen, alles loslassen – pls massage my soul.",
                "B": "Ich brauch Action! Schwitzen, stretchen, strong AF werden.",
                "C": "Beides irgendwie? Flowen UND chillen?!",
                "D": "Ich will langsam reingleiten und schauen, wo mein Körper gerade Bock hat."
            }
        },
        {
            "id": 5,
            "question": "Wie willst du dein Yoga erleben?",
            "answers": {
                "A": "Kollektiver Vibe, alle zusammen: like a Sunday Brunch – nur mit Asanas.",
                "B": "Selfmade Queen: Ich will mein Tempo, aber mit Support!",
                "C": "Netflix-Yoga: Ich mach mein eigenes Ding, Hauptsache gemütlich.",
                "D": "Ich brauch klare Ansagen – step by step, sonst verlauf ich mich."
            }
        }
    ]

    # Shuffle questions only once and store them in the session
    if 'shuffled_questions' not in request.session:
        random.shuffle(questions)
        request.session['shuffled_questions'] = questions
        request.session['current_question_index'] = 0
        request.session['responses'] = []

    # Handle answer submission
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer:
            # Log the response
            responses = request.session.get('responses', [])
            responses.append(answer)
            request.session['responses'] = responses

            # Move to the next question
            request.session['current_question_index'] += 1

            # Check if there are more questions
            if request.session['current_question_index'] >= len(request.session['shuffled_questions']):
                return redirect('result')  # Redirect to the result page

    # Get the current question
    current_index = request.session.get('current_question_index', 0)

    # Check if the index is valid
    if current_index >= len(request.session['shuffled_questions']):
        return redirect('result')  # Redirect to the result page

    current_question = request.session['shuffled_questions'][current_index]

    return render(request, 'questionnaire.html', {'question': current_question})

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
    # Mapping of answers to yoga types
    answer_to_yoga_type = {
        "A": "Burnout-Yogini",
        "B": "Ashtanga-Warrior",
        "C": "Homeoffice-Yogi",
        "D": "Casual-Stretcher",
    }

    # Retrieve the user's responses from the session
    responses = request.session.get('responses', [])

    # Count the occurrences of each yoga type
    yoga_type_count = {}
    for answer in responses:
        yoga_type = answer_to_yoga_type.get(answer)
        if yoga_type:
            yoga_type_count[yoga_type] = yoga_type_count.get(yoga_type, 0) + 1

    # Determine the most frequent yoga type
    result_yoga_type = max(yoga_type_count, key=yoga_type_count.get, default="Unbekannt")

    # Store the result type in the session
    request.session['result_type'] = result_yoga_type

    # Pass the result to the template
    return render(request, 'result.html', {'result_text': f"Dein Yoga-Typ ist: <strong>{result_yoga_type}</strong>!", 'result_type': result_yoga_type})

def recommended_classes(request):
    """
    Display recommended classes based on the user's result type.
    """
    # Mapping of result types to their type keys
    result_type_to_key = {
        "Burnout-Yogini": "A",
        "Ashtanga-Warrior": "B",
        "Homeoffice-Yogi": "C",
        "Casual-Stretcher": "D",
    }

    # List of classes
    classes = [
        {"name": "Kindness-Kurs für Anfänger", "description": "Basic Einführung, ohne Druck, Basics wie Atmen, achtsames Spüren", "duration": "60 min", "type": "D"},
        {"name": "Basic Kindness", "description": "Offene Stunde für Anfänger:innen & Wiedereinsteiger:innen, sanfte Bewegungen", "duration": "60 min", "type": "D"},
        {"name": "Yin Kindness", "description": "Langsame, passive Haltungen, Raum zum Spüren und Loslassen", "duration": "60 min", "type": "A"},
        {"name": "Yin Extended Kindness (SO)", "description": "Verlängerte Yin Yoga Session mit noch mehr Raum für Ruhe", "duration": "75 min", "type": "A"},
        {"name": "Ashtanga Kindness", "description": "Strukturierte Ashtanga-Praxis ohne Leistungsdruck", "duration": "75 min", "type": "B"},
        {"name": "Ashtanga Practice Kindness (Self Practice)", "description": "Selbständige Ashtanga-Praxis mit achtsamer Begleitung", "duration": "120 min", "type": "B"},
        {"name": "Vinyasa Kindness", "description": "Achtsamer Flow, kraftvoll und sanft, im Rhythmus des Atems", "duration": "60 min", "type": "C"},
        {"name": "Be Kind Flow (Slow Flow/Basic Flow)", "description": "Sanfter Flow ohne Vinyasas – entspannt, kreativ, bewusst", "duration": "60 min", "type": "C"},
        {"name": "Rainbow Kindness-Vinyasa Special", "description": "Vinyasa Flow kombiniert mit Farben und Musik", "duration": "75–90 min", "type": "C"},
        {"name": "Music Kindness-Vinyasa Special", "description": "Flow im Rhythmus eines Musikthemas/Künstlers", "duration": "75–90 min", "type": "C"},
        {"name": "The Yin of Kindness", "description": "Kombination aus Yin Yoga & Yoga Nidra (tiefes Loslassen)", "duration": "90 min", "type": "A"},
        {"name": "The Kind Flow of Words", "description": "Yoga mit intuitivem Schreiben und Poesie", "duration": "90 min", "type": "A"},
        {"name": "Karma & Kindness (Soft Satsang)", "description": "Sanfter Deep Talk über Yoga-Philosophie und Alltagsthemen", "duration": "60 min", "type": "A"},
        {"name": "1:1 Kindness Yoga", "description": "Private Einzelstunde für individuelle Praxis", "duration": "60 min", "type": "C"},
        {"name": "Traumasensibles 1:1 Kindness Yoga", "description": "Traumainformierte Einzelbegleitung in deinem Tempo", "duration": "60 min", "type": "A"},
        {"name": "Kindness under the Moon (Workshop)", "description": "Neumond/Vollmond Zeremonie mit Yoga, Journaling, Ritualen", "duration": "2,5–3 h", "type": "A"},
        {"name": "Be Kind Safe Space Abend (Workshop)", "description": "Kakao, Sharing Circles, Ankommen im eigenen Raum", "duration": "2,5–3 h", "type": "A"},
        {"name": "Be Kind Brave Space Abend (Workshop)", "description": "Sanftes Wachsen an inneren Grenzen, mutiges Lernen", "duration": "2,5–3 h", "type": "B"},
        {"name": "Fuck-Up Session: Asana Fuck-Ups & Lebenslektionen", "description": "Ego loslassen auf und neben der Matte", "duration": "2–2,5 h", "type": "B"},
    ]

    # Get the user's result type from the session
    result_type = request.session.get('result_type', None)

    # Map the result type to its corresponding type key
    type_key = result_type_to_key.get(result_type)

    # Filter classes based on the type key
    filtered_classes = [cls for cls in classes if cls["type"] == type_key]

    return render(request, 'recommended_classes.html', {'classes': filtered_classes, 'result_type': result_type})