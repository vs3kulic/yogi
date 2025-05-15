"""
Module for utility functions and classes used in the questionnaire application.
This module includes a session manager class to handle session-related operations,
"""


class SessionManager:
    """
    A utility class to manage session-related operations for the questionnaire.
    """

    def __init__(self, session):
        self.session = session

    def reset_questionnaire(self):
        """
        Clears all questionnaire-related session data.
        """
        for key in ('shuffled_questions', 'current_question_index', 'responses', 'result_type'):
            self.session.pop(key, None)

    def initialize_questionnaire(self, num_questions):
        """
        Ensures session variables are initialized for the questionnaire.
        """
        if 'responses' not in self.session:
            self.session['responses'] = [None] * num_questions
        if 'current_question_index' not in self.session:
            self.session['current_question_index'] = 0

    def get_current_question_index(self):
        """
        Retrieves the current question index from the session.
        """
        return self.session.get('current_question_index', 0)

    def set_current_question_index(self, index):
        """
        Updates the current question index in the session.
        """
        self.session['current_question_index'] = index

    def get_responses(self):
        """
        Retrieves the responses from the session.
        """
        return self.session.get('responses', [])

    def save_response(self, index, answer):
        """
        Saves a response for a specific question index.
        """
        responses = self.get_responses()
        responses[index] = answer
        self.session['responses'] = responses

