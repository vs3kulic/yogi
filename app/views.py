"""
views.py module contains the logic for handling user requests and rendering appropriate responses.
"""

import logging
import json
import requests
import os
import markdown
import unicodedata
import re
import random
import uuid  # For generating unique session IDs
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.cache import cache
from django.db import IntegrityError
from django.db import models
from .models import YogaClass, QuestionnaireResult, OllamaResponse
from .utils import SessionManager
from .constants import ANSWER_TO_TYPE, YOGA_RESULT_TYPES, QUESTIONS


logger = logging.getLogger(__name__)

# ---------------------------
# Load Questions
# ---------------------------
def load_questions():
    """Load questions from JSON file or fall back to constants"""
    file_path = os.path.join(settings.BASE_DIR, 'app', 'data', 'questions.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            questions = json.load(file)
        return questions
    except Exception as e:
        logger.error("Error loading questions from JSON: %s", e)
        logger.info("Using questions from constants.py as fallback")
        
        # Convert constants format to JSON format for template consistency
        formatted_questions = []
        for q in QUESTIONS:
            answers = []
            for key, text in q['answers'].items():
                answers.append({
                    "text": text,
                    "value": key
                })
            
            formatted_questions.append({
                "id": q['number'],
                "text": q['question'],
                "answers": answers
            })
            
        return formatted_questions

# ---------------------------
# Home and Static Views
# ---------------------------
@require_GET
def index(request):
    """
    Home page view.
    """
    return render(request, 'index.html')


@require_GET
def info(request):
    """
    Renders a static info/lore page.
    """
    return render(request, 'info.html')


@require_GET
def robots_txt(_request):
    """
    Serve the robots.txt file to control web crawler access.
    """
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# ---------------------------
# Questionnaire Views
# ---------------------------
@require_http_methods(["GET", "POST"])
def questionnaire(request):
    """
    Handles the questionnaire flow: displaying questions, saving answers, and navigation.
    """
    # Generate a unique session ID if not already set
    session_id = request.session.get('session_id')
    if not session_id:
        session_id = str(uuid.uuid4())
        request.session['session_id'] = session_id

    session_data = request.session.get('questionnaire', {})
    answers = session_data.get('answers', [])
    current_question_index = session_data.get('current_question', 1)

    questions = load_questions()
    total_questions = len(questions)

    if request.method == 'POST':
        answer = request.POST.get('answer')
        
        if answer:
            if len(answers) >= current_question_index:
                answers[current_question_index - 1] = answer
            else:
                answers.append(answer)
                
            if current_question_index < total_questions:
                current_question_index += 1
                request.session['questionnaire'] = {
                    'answers': answers,
                    'current_question': current_question_index
                }
            else:
                # Calculate the result
                result = calculate_result_from_answers(answers)

                # Save the result to the database
                try:
                    QuestionnaireResult.objects.create(
                        session_id=session_id,
                        answers=answers,
                        result_type=result
                    )
                except IntegrityError:
                    # Handle duplicate session_id by generating a new one
                    session_id = str(uuid.uuid4())
                    request.session['session_id'] = session_id
                    QuestionnaireResult.objects.create(
                        session_id=session_id,
                        answers=answers,
                        result_type=result
                    )

                request.session['questionnaire'] = {
                    'answers': answers,
                    'result': result
                }
                return redirect('result')

    question_index = current_question_index - 1
    question = questions[question_index] if question_index < len(questions) else None

    progress = (current_question_index - 1) / (total_questions - 1) * 100 if total_questions > 1 else 100

    context = {
        'question': question,
        'progress': progress,
        'current_question': current_question_index,
        'total_questions': total_questions,
    }

    return render(request, 'questionnaire.html', context)

@require_POST
def reset_questionnaire(request):
    """
    Resets the questionnaire session and redirects to home.
    """
    session_manager = SessionManager(request.session)
    session_manager.reset_questionnaire()
    return redirect('index')

# ---------------------------
# Result Views
# ---------------------------

@require_GET
def recommended_classes(request):
    """
    Displays recommended classes based on the user's result type.
    """
    result_type = request.session.get('result_type')
    filtered_classes = YogaClass.objects.filter(yoga_type=result_type)
    return render(request, 'recommended_classes.html', {
        'classes': filtered_classes,
        'result_type': result_type
    })

@require_GET
def calculate_result(request):
    """
    Calculates the user's yoga type based on their answers.
    """
    session_manager = SessionManager(request.session)
    responses = session_manager.get_responses()
    result_yoga_type = calculate_result_from_answers(responses)
    request.session['result_type'] = result_yoga_type

    return render(request, 'result.html', {
        'result_text': f"Your yoga type is: <strong>{result_yoga_type}</strong>!",
        'result_type': result_yoga_type
    })

def calculate_result_from_answers(answers):
    """
    Helper function to calculate yoga type from answers.
    """
    type_counts = {}
    for resp in answers:
        result_type = ANSWER_TO_TYPE.get(resp)
        if result_type:
            type_counts[result_type] = type_counts.get(result_type, 0) + 1

    return max(type_counts, key=type_counts.get, default="Casual-Stretcher")

# ---------------------------
# Subscription Views
# ---------------------------

# subscribe_view
@require_http_methods(["POST"])
def subscribe_view(request):
    """
    Helper function to subscribe an email address to Mailchimp.

    Args:
        request (HttpRequest): The HTTP request object containing the email address.
    Returns:
        JsonResponse: A JSON response indicating success or failure.
    """
    email = request.POST.get("email")

    if not email:
        return JsonResponse({"error": "Email is required."}, status=400)
    
    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({"error": "Invalid email format."}, status=400)

    # Call the subscribe_email function to process the subscription
    status_code, response = subscribe_email(email)

    # Check the status code and response
    if 200 <= status_code < 300:
        return JsonResponse({"message": "Successfully subscribed!"}, status = status_code)
    else:
        error_msg = response.get("detail") if isinstance(response, dict) else "Subscription failed."
        return JsonResponse({"error": error_msg}, status = status_code)


def subscribe_email(email):
    """
    Helper function to subscribe an email address to Mailchimp.

    Args:
        email (str): The email address to subscribe.
        
    Returns:
        tuple: (status_code, response)
            status_code (int): HTTP status code from Mailchimp API.
            response (dict): JSON response from Mailchimp API.
    """
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    try:
        # Send a POST request to Mailchimp API
        req = requests.post(
            settings.MAILCHIMP_MEMBERS_ENDPOINT,
            auth=("", settings.MAILCHIMP_API_KEY),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        try:
            resp_json = req.json()  # Attempt to decode JSON response
        except ValueError:
            resp_json = {}  # Fallback to empty dict if JSON decoding fails
        
        return req.status_code, resp_json

    except requests.RequestException as e:
        # Handle request-related exceptions (e.g., connection errors, timeouts)
        return 503, {"detail": str(e)}

def yoga_classes_api(request):
    """API endpoint for yoga classes using JSON data"""
    try:
        # Get result type from session if it exists
        result_type = request.session.get('result_type', None)
        
        # Load yoga classes from JSON file
        json_path = os.path.join(settings.BASE_DIR, 'app', 'data', 'yoga_classes.json')
        
        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                all_classes = json.load(file)
                
            # Filter classes by result type if specified
            if result_type:
                classes = [cls for cls in all_classes if cls.get('yoga_type') == result_type]
            else:
                classes = all_classes
                
        except (FileNotFoundError, json.JSONDecodeError):
            # If JSON file doesn't exist or is invalid, return an empty list
            classes = []

        return JsonResponse(classes, safe=False)
    
    except Exception as e:
        # Log the error
        logger = logging.getLogger(__name__)
        logger.error("Error in yoga_classes_api: %s", str(e))
        return JsonResponse({"error": "An error occurred while processing the request."}, status=500)

# ---------------------------
# Ollama API View
# ---------------------------

def ollama_view(request):
    """
    Renders the result page with the calculated yoga type and its details.
    """
    logger = logging.getLogger(__name__)

    # Get result type from session or default to "Casual-Stretcher"
    result_type = request.session.get('questionnaire', {}).get('result', 'Casual-Stretcher')
    logger.info(f"Result type: {result_type}")

    # Get the detailed result information from the constants
    result_data = YOGA_RESULT_TYPES.get(result_type, {
        'title': 'Unknown',
        'description': ['No description available.'],
        'match': {'title': 'None', 'reason': 'No match found.'},
        'challenge': {'title': 'None', 'reason': 'No challenge found.'}
    })

    # Ensure description is a single string with proper spacing
    if isinstance(result_data['description'], list):
        result_data['description'] = ' '.join(result_data['description'])
    
    # Get the session ID from the request
    session_id = request.session.get('session_id', None)
    if not session_id:
        logger.error("Session ID not found.")
        return JsonResponse({"error": "Session ID not found. Please start the questionnaire."}, status=400)

    logger.info(f"Session ID: {session_id}")

    # Fetch the Result from the QuestionnaireResult table
    try:
        questionnaire_result = QuestionnaireResult.objects.get(session_id=session_id)
        logger.info(f"Fetched QuestionnaireResult: {questionnaire_result}")
    except QuestionnaireResult.DoesNotExist:
        logger.error(f"No QuestionnaireResult found for session_id: {session_id}")
        return JsonResponse({"error": "Questionnaire result not found."}, status=404)
    
    # Get the user's answers from the QuestionnaireResult table
    user_answers = questionnaire_result.answers  # Example: ["A", "C", "B", "A", "C"]
    logger.info(f"User answers: {user_answers}")

    # Fetch the matching OllamaResponse based on the combinations field
    ollama_response = OllamaResponse.objects.filter(combinations=user_answers).first()
    if not ollama_response:
        logger.warning(f"No OllamaResponse found for answers: {user_answers}")
        pro_tip = "Oje, ich konnte keinen Tipp für dich erstellen :/"
    else:
        # Use response_de if available, otherwise fallback to response
        ollama_response_text = ollama_response.response_de or ollama_response.response
        pro_tip = clean_text(ollama_response_text)
        logger.info(f"Fetched OllamaResponse: {ollama_response_text}")

    # Pass pro_tip to the result template
    return render(request, 'result.html', {
        'pro_tip': pro_tip,
        'result_type': result_type,
        'result_data': result_data,
        'session_id': session_id
    })

def clean_text(text):
    """
    Cleans up the response text by normalizing spaces, removing special characters, 
    fixing formatting, and removing stars (*).
    """
    # Normalize unicode characters
    text = unicodedata.normalize("NFKC", text)

    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text)

    # Remove unnecessary spaces around punctuation
    text = re.sub(r"\s([?.!’,;](?:\s|$))", r"\1", text)

    # Remove stars (*)
    text = text.replace("*", "")

    # Fix broken words (e.g., "cal ms" -> "calms")
    # Fix broken words (e.g., "Pra na ya ma" -> "Pranayama")
    text = re.sub(r"\b(\w+)\s(\w+)\b", lambda m: m.group(1) + m.group(2) if m.group(1) + m.group(2) in ["calms", "anchors"] else m.group(0), text)
    text = re.sub(r"\b(Pra)\s(na)\s(ya)\s(ma)\b", r"\1\2\3\4", text, flags=re.IGNORECASE)

    # Remove space before a period
    text = re.sub(r"\s+\.", ".", text)

    # Strip leading and trailing spaces
    return text.strip()

def example_view(request):
    """
    Example view to demonstrate the usage of the square function.
    """
    number = 5
    squared_value = square(number)  # Call the square function
    return render(request, 'info.html', {
        'number': number,
        'squared_value': squared_value
    })
