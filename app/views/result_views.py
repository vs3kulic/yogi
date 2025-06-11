"""This module contains the view for calculating and displaying the user's yoga type result.

It processes the user's answers, retrieves relevant data from the database,
and renders the result page with the calculated yoga type and additional tips.
"""
import logging
from django.shortcuts import render
from django.views.decorators.http import require_GET
from app.utils import calculate_result_from_answers
from app.constants import YOGA_RESULT_TYPES, DEFAULT_YOGA_TYPE

logger = logging.getLogger(__name__)

@require_GET
def calculate_result(request):
    """
    Calculates the user's yoga type and fetches the pro_tip.
    """
    session_data = request.session.get('questionnaire', {})
    answers = session_data.get('answers', [])
    logger.info(f"Session answers in calculate_result: {answers}")

    # Calculate the yoga type based on responses
    result_yoga_type = calculate_result_from_answers(answers)
    request.session['result_type'] = result_yoga_type

    key = result_yoga_type if result_yoga_type is not None else DEFAULT_YOGA_TYPE
    result_data = YOGA_RESULT_TYPES.get(key, {})

    # Pass context variables to the result template
    return render(request, 'result.html', {
        'result_text': f"Your yoga type is: <strong>{result_yoga_type}</strong>!",
        'result_type': result_yoga_type,
        'result_data': result_data,
        'pro_tip': "Stay hydrated and practice mindfulness!",  # Example pro_tip
    })
