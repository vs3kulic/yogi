"""
views.py module contains the logic for handling user requests and rendering appropriate responses.
"""
import logging
import json
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import YogaClass  # Adjust import path as needed
from .utils import SessionManager
from .constants import QUESTIONS, ANSWER_TO_TYPE

logger = logging.getLogger(__name__)


# ---------------------------
# Views
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


@require_GET
def index(request):
    """
    Home page view. Resets questionnaire session data.
    """
    session_manager = SessionManager(request.session)
    session_manager.reset_questionnaire()
    return render(request, 'index.html')

@require_GET
def info(request):
    """
    Renders a static info/lore page.
    """
    return render(request, 'info.html')

@require_http_methods(["GET", "POST"])
def questionnaire(request):
    """
    Handles the questionnaire flow: displaying questions, saving answers, and navigation.
    """
    session_manager = SessionManager(request.session)
    session_manager.initialize_questionnaire(len(QUESTIONS))

    current_index = session_manager.get_current_question_index()
    responses = session_manager.get_responses()

    if request.method == "POST":
        if 'back' in request.POST:
            if current_index > 0:
                session_manager.set_current_question_index(current_index - 1)
            return redirect('questionnaire')

        answer = request.POST.get("answer")
        if answer:
            session_manager.save_response(current_index, answer)
            next_index = current_index + 1

            if next_index >= len(QUESTIONS):
                return redirect('calculate_result')

            session_manager.set_current_question_index(next_index)
            return redirect('questionnaire')

    # Render current question
    question = QUESTIONS[current_index]
    return render(request, 'questionnaire.html', {
        'question': question,
        'current_question_index': current_index + 1,  # 1-based for display
        'total_questions': len(QUESTIONS),
    })

@require_POST
def reset_questionnaire(request):
    """
    Resets the questionnaire session and redirects to home.
    """
    session_manager = SessionManager(request.session)
    session_manager.reset_questionnaire()
    return redirect('index')

@require_GET
def calculate_result(request):
    """
    Calculates the user's yoga type based on their answers.
    """
    session_manager = SessionManager(request.session)
    responses = session_manager.get_responses()

    # Tally results
    type_counts = {}
    for resp in responses:
        result_type = ANSWER_TO_TYPE.get(resp)
        if result_type:
            type_counts[result_type] = type_counts.get(result_type, 0) + 1

    result_yoga_type = max(type_counts, key=type_counts.get, default="Unbekannt")
    request.session['result_type'] = result_yoga_type

    return render(request, 'result.html', {
        'result_text': f"Dein Yoga-Typ ist: <strong>{result_yoga_type}</strong>!",
        'result_type': result_yoga_type
    })

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
