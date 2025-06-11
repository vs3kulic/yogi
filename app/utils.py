"""Module for utility functions and classes used in the questionnaire application.
This module includes a session manager class to handle session-related operations,
"""
import os
import json
import random
import logging
from collections import Counter
from django.shortcuts import render, redirect
from django.conf import settings
from django.views.decorators.http import require_GET
from app.constants import ANSWER_TO_TYPE, DEFAULT_YOGA_TYPE, YOGA_RESULT_TYPES

logger = logging.getLogger(__name__)

def load_questions():
    file_path = os.path.join(settings.BASE_DIR, 'app', 'data', 'questions.json')
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            questions = json.load(file)
        return questions
    except Exception as e:
        print(f"Error loading questions: {e}")
        return []

def calculate_result_from_answers(answers):
    """
    Calculates the user's yoga type based on their answers.
    """
    logger.info(f"Answers received: {answers}")
    result_types = [ANSWER_TO_TYPE.get(resp) for resp in filter(None, answers) if ANSWER_TO_TYPE.get(resp)]
    type_counts = Counter(result_types)
    logger.info(f"Type Counts: {type_counts}")

    if not type_counts:
        return DEFAULT_YOGA_TYPE  # Use the default yoga type

    max_count = max(type_counts.values())
    candidates = [k for k, v in type_counts.items() if v == max_count]
    return random.choice(candidates)  # Handle ties randomly

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

    # Debugging: Log the session state
    logger.info(f"Session responses after saving: {request.session['responses']}")
    logger.info(f"Session key before redirect: {request.session.session_key}")

    # Redirect to the next question or result page
    if current_index + 1 >= len(request.session['responses']):
        return redirect('result')  # Redirect to the result page
    return redirect('questionnaire')  # Redirect to the next question

@require_GET
def calculate_result(request):
    """
    Calculates the user's yoga type and fetches the pro_tip.
    """
    logger.info(f"Session keys: {list(request.session.keys())}")
    logger.info(f"Session key after redirect: {request.session.session_key}")
    responses = request.session.get('responses', [])
    logger.info(f"Session responses in calculate_result: {responses}")

    # Calculate the yoga type based on responses
    result_yoga_type = calculate_result_from_answers(responses)
    request.session['result_type'] = result_yoga_type

    # Ensure result_yoga_type is a string before using as a key
    key = result_yoga_type if result_yoga_type is not None else DEFAULT_YOGA_TYPE
    result_data = YOGA_RESULT_TYPES.get(key, {})

    # Pass context variables to the result template
    return render(request, 'result.html', {
        'result_text': f"Your yoga type is: <strong>{result_yoga_type}</strong>!",
        'result_type': result_yoga_type,
        'result_data': result_data,
        'pro_tip': "Stay hydrated and practice mindfulness!",  # Example pro_tip
    })
