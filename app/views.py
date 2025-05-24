"""
views.py module contains the logic for handling user requests and rendering appropriate responses.
"""
import logging
import json
import requests
import os
from django.shortcuts import render, redirect  # Make sure redirect is imported
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.core.validators import validate_email
from .models import YogaClass  # Make sure this import is present
from .utils import SessionManager
from .constants import ANSWER_TO_TYPE, YOGA_RESULT_TYPES  # Import constants as fallback

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
    Home page view.
    """
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
    # Get the session or create a new one
    session_data = request.session.get('questionnaire', {})
    answers = session_data.get('answers', [])
    current_question_index = session_data.get('current_question', 1)

    # Load questions from JSON file or fall back to constants
    questions = load_questions()
    total_questions = len(questions)

    # Check if we're submitting an answer
    if request.method == 'POST':
        answer = request.POST.get('answer')
        
        if answer:
            # Update answers list
            if len(answers) >= current_question_index:
                answers[current_question_index - 1] = answer
            else:
                answers.append(answer)
                
            # Move to next question or show results
            if current_question_index < total_questions:
                current_question_index += 1
                request.session['questionnaire'] = {
                    'answers': answers,
                    'current_question': current_question_index
                }
            else:
                # Calculate result and redirect
                result = calculate_yoga_type(answers)
                request.session['questionnaire'] = {
                    'answers': answers,
                    'result': result
                }
                return redirect('result')

    # Get the current question
    question_index = current_question_index - 1
    question = questions[question_index] if question_index < len(questions) else None

    # Calculate progress percentage
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


def load_questions():
    """Load questions from JSON file or fall back to constants"""
    file_path = os.path.join(settings.BASE_DIR, 'app', 'data', 'questions.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            questions = json.load(file)
        return questions
    except Exception as e:
        print(f"Error loading questions from JSON: {e}")
        print("Using questions from constants.py as fallback")
        
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

def calculate_yoga_type(answers):
    """
    Calculate the yoga type based on the most frequent answer choice.
    
    Args:
        answers: List of answer values (e.g., ['A', 'B', 'C', 'A', 'A'])
        
    Returns:
        String representing the yoga type
    """
    # Count the occurrences of each answer type
    answer_counts = {}
    for answer in answers:
        if answer in answer_counts:
            answer_counts[answer] += 1
        else:
            answer_counts[answer] = 1

    # Find the most frequent answer
    if answer_counts:
        max_answer = max(answer_counts, key=answer_counts.get)
    else:
        max_answer = None  # Handle case where no answers are provided

    # Map to yoga type
    return ANSWER_TO_TYPE.get(max_answer, "Casual-Stretcher")

def result(request):
    """
    Renders the result page with the calculated yoga type and its details.
    """
    # Get result type from session or default to "Casual-Stretcher"
    result_type = request.session.get('questionnaire', {}).get('result', 'Casual-Stretcher')

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

    return render(request, 'result.html', {
        'result_type': result_type,
        'result_data': result_data
    })

@require_GET
def debug_index(request):
    """
    Debug version of the home page.
    """
    return render(request, 'index_debug.html')

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
                
            # If no classes found (or file empty), use fallback data
            if not classes:
                classes = get_fallback_classes()
        except (FileNotFoundError, json.JSONDecodeError):
            # If JSON file doesn't exist or is invalid
            classes = get_fallback_classes()
            
        return JsonResponse(classes, safe=False)
    
    except Exception as e:
        # Log the error
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Error in yoga_classes_api: {str(e)}")
        
        # Return fallback data
        return JsonResponse(get_fallback_classes(), safe=False)

def get_fallback_classes():
    """Return some fallback yoga classes"""
    return [
        {
            "id": 1,
            "name": "Vinyasa Flow",
            "description": "Ein dynamischer Yoga-Stil, der Atmung und Bewegung verbindet.",
            "yoga_type": "vinyasa",
            "intensity": "mittel",
            "duration": 60
        },
        {
            "id": 2,
            "name": "Yin Yoga",
            "description": "Eine ruhige Praxis mit längeren Haltungen für tiefe Entspannung.",
            "yoga_type": "yin",
            "intensity": "niedrig",
            "duration": 75
        },
        {
            "id": 3,
            "name": "Power Yoga",
            "description": "Eine kraftvolle und herausfordernde Yoga-Praxis.",
            "yoga_type": "power",
            "intensity": "hoch",
            "duration": 60
        }
    ]

def test_questions(request):
    """Test endpoint to verify questions.json is loading correctly"""
    try:
        json_path = os.path.join(settings.BASE_DIR, 'app', 'data', 'questions.json')
        with open(json_path, 'r', encoding='utf-8') as file:
            questions = json.load(file)
        return JsonResponse(questions, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def debug_questions(request):
    """
    Debug page to display questions.json content directly
    """
    try:
        # Get absolute path to the JSON file
        json_path = os.path.join(settings.BASE_DIR, 'app', 'data', 'questions.json')
        
        # Check if file exists
        if not os.path.exists(json_path):
            return HttpResponse(f"ERROR: File not found at: {json_path}", content_type="text/plain")
        
        # Try to read the file content
        with open(json_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Try to parse the JSON
        try:
            questions = json.loads(content)
            # Return formatted JSON and raw content for debugging
            response = f"""
            <html>
            <head><title>Debug Questions</title></head>
            <body>
                <h1>Debug Questions</h1>
                <h2>File Path</h2>
                <pre>{json_path}</pre>
                
                <h2>Raw Content</h2>
                <pre>{content}</pre>
                
                <h2>Parsed Questions ({len(questions)} found)</h2>
                <pre>{json.dumps(questions, indent=2)}</pre>
            </body>
            </html>
            """
            return HttpResponse(response)
        except json.JSONDecodeError as e:
            return HttpResponse(f"JSON Parse Error: {str(e)}\n\nContent:\n{content}", content_type="text/plain")
    except Exception as e:
        import traceback
        return HttpResponse(f"Error: {str(e)}\n\n{traceback.format_exc()}", content_type="text/plain")

def test_json(request):
    """Ultra simple test to check if JSON is loading"""
    try:
        path = os.path.join(settings.BASE_DIR, 'app', 'data', 'questions.json')
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return JsonResponse({"success": True, "questions_count": len(data), "data": data})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)

def debug_file_access(request):
    """Debug file access permissions"""
    response = []
    
    # Check if data directory exists
    data_dir = os.path.join(settings.BASE_DIR, 'app', 'data')
    response.append(f"Data directory exists: {os.path.exists(data_dir)}")
    
    # List files in data directory
    try:
        files = os.listdir(data_dir)
        response.append(f"Files in data directory: {files}")
    except Exception as e:
        response.append(f"Error listing files: {str(e)}")
    
    # Check questions.json specifically
    json_path = os.path.join(data_dir, 'questions.json')
    response.append(f"questions.json exists: {os.path.exists(json_path)}")
    
    # Try to create a test file
    test_path = os.path.join(data_dir, 'test_write.txt')
    try:
        with open(test_path, 'w') as f:
            f.write("Test write access")
        response.append("Successfully created test file")
    except Exception as e:
        response.append(f"Error creating test file: {str(e)}")
    
    return HttpResponse("<br>".join(response))

def result_view(request):
    # Get the result type from session or however you're currently determining it
    result_type = request.session.get('result_type', 'Ashtanga-Warrior')
    
    # Get the result details from the constants
    result_details = YOGA_RESULT_TYPES.get(result_type, YOGA_RESULT_TYPES['Ashtanga-Warrior'])
    
    context = {
        'result_type': result_type,
        'result': result_details  # Pass the entire result object to the template
    }
    
    return render(request, 'result.html', context)
