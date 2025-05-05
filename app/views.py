import random
import os
import logging
import requests
import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from app.models import YogaClass

logger = logging.getLogger(__name__)

# Mailchimp configuration
MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_LIST_ID = settings.MAILCHIMP_LIST_ID
MAILCHIMP_DC = settings.MAILCHIMP_DC

# Mailchimp endpoint
members_endpoint = f"https://{MAILCHIMP_DC}.api.mailchimp.com/3.0/lists/{MAILCHIMP_LIST_ID}/members"

def subscribe_email(email):
    """
    Subscribe an email address to a Mailchimp list.

    Args:
        email (str): The email address to subscribe.

    Returns:
        tuple: A tuple containing the HTTP status code and the response JSON.
    """
    data = {
        "email_address": email,
        "status": "subscribed"
    }

    req = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data),
        headers={"Content-Type": "application/json"}
    )

    return req.status_code, req.json()

def subscribe_view(request):
    """
    Handle email subscription requests from the result page.
    """
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            status_code, response = subscribe_email(email)
            if status_code == 200:
                return JsonResponse({"message": "Successfully subscribed!"}, status=200)
            else:
                return JsonResponse({"error": response.get("detail", "Subscription failed.")}, status=status_code)
        return JsonResponse({"error": "Email is required."}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=405)

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
    Handle the questionnaire logic where users move forward by selecting an answer
    or backward using a Back button.
    """
    # Define the questions
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

    # Initialize session variables if not already set
    if 'responses' not in request.session:
        request.session['responses'] = [None] * len(questions)  # Pre-fill with None
    if 'current_question_index' not in request.session:
        request.session['current_question_index'] = 0

    # Handle POST request
    if request.method == "POST":
        # Check if the user clicked the Back button
        if 'back' in request.POST:
            current_question_index = request.session['current_question_index']
            if current_question_index > 0:
                request.session['current_question_index'] -= 1
            return redirect('questionnaire')

        # Handle answer submission
        answer = request.POST.get("answer")
        if answer:
            # Save the answer at the correct index
            current_question_index = request.session['current_question_index']
            responses = request.session['responses']
            responses[current_question_index] = answer  # Update the response for the current question
            request.session['responses'] = responses

            # Move to the next question
            current_question_index += 1
            request.session['current_question_index'] = current_question_index

            # Redirect to the result page if all questions are answered
            if current_question_index >= len(questions):
                return redirect('calculate_result')

    # Get the current question index
    current_question_index = request.session['current_question_index']

    # Render the current question
    question = questions[current_question_index]
    return render(request, 'questionnaire.html', {
        'question': question,
        'current_question_index': current_question_index + 1,  # For display (1-based index)
        'total_questions': len(questions),
    })

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
