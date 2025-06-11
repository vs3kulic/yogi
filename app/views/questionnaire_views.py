"""This module handles the questionnaire views, including displaying questions,
saving answers, and managing the questionnaire session.
"""
import uuid
import os
import json
import logging
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.db import IntegrityError
from django.conf import settings
from app.models import QuestionnaireResult
from app.utils import calculate_result_from_answers
from app.constants import QUESTIONS

logger = logging.getLogger(__name__)

def initialize_questionnaire(request, num_questions):
    """
    Initializes session variables for the questionnaire.
    """
    request.session['responses'] = [None] * num_questions
    request.session['current_question_index'] = 0
    request.session.modified = True

def load_questions():
    """
    Load questions from a JSON file or fall back to constants.
    """
    file_path = os.path.join(settings.BASE_DIR, 'app', 'data', 'questions.json')
    try:
        # Attempt to load questions from the JSON file
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback to constants if JSON file cannot be loaded
        return [
            {
                "id": q["number"],
                "text": q["question"],
                "answers": [{"text": text, "value": key} for key, text in q["answers"].items()]
            }
            for q in QUESTIONS
        ]

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
    Clears all questionnaire-related session data.
    """
    for key in ('responses', 'current_question_index', 'result_type'):
        request.session.pop(key, None)
    request.session.modified = True

def submit_question(request):
    """
    Handles the submission of a questionnaire answer.
    """
    current_index = request.session.get('current_question_index', 0)
    answer = request.POST.get('answer')  # Retrieve the submitted answer

    # Initialize responses if not already set
    if 'responses' not in request.session:
        num_questions = 5  # Replace with the actual number of questions
        request.session['responses'] = [None] * num_questions

    # Save the response
    responses = request.session['responses']
    responses[current_index] = answer
    request.session['responses'] = responses
    request.session['current_question_index'] = current_index + 1  # Move to the next question
    request.session.modified = True  # Ensure session changes are saved
    request.session.save()
    logger.info(f"Session responses after saving: {request.session['responses']}")
