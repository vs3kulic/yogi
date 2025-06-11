from unittest.mock import patch
import requests
from django.test import TestCase
from app.views.subscription_views import subscribe_email

class SubscribeEmailTests(TestCase):
    """
    This test suite covers the functionality of the subscribe_email function,
    including successful subscription, handling of invalid JSON responses,
    and exceptions during the API call.
    """

    @patch('app.views.subscription_views.subscribe_email')  # Mock the subscribe_email function
    def test_subscribe_email_success(self, mock_subscribe):
        """
        Test subscribe_email with a successful Mailchimp API response.
        """
        # Mock the API response
        mock_subscribe.return_value = (200, {"message": "Successfully subscribed!"})

        # Call the function
        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 200)
        self.assertEqual(response, {"message": "Successfully subscribed!"})

    @patch('app.views.subscription_views.subscribe_email')
    def test_subscribe_email_failure(self, mock_subscribe):
        """
        Test subscribe_email with a Mailchimp API failure (503 Service Unavailable).
        """
        # Mock the API response
        mock_subscribe.return_value = (503, {"detail": "Service unavailable."})

        # Call the function
        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 503)
        self.assertEqual(response, {"detail": "Service unavailable."})

    @patch('app.views.subscription_views.subscribe_email')
    def test_subscribe_email_invalid_json(self, mock_subscribe):
        """
        Test subscribe_email when the Mailchimp API returns invalid JSON.
        """
        # Mock the API response
        mock_subscribe.return_value = (200, {})  # Simulate invalid JSON response

        # Call the function
        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 200)
        self.assertEqual(response, {})  # Fallback to an empty dictionary

    @patch('app.views.subscription_views.subscribe_email', side_effect=requests.exceptions.ConnectionError("Connection error"))
    def test_subscribe_email_exception(self, mock_subscribe):
        """
        Test subscribe_email when a ConnectionError is raised during the API call.
        """
        # Call the function
        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 503)
        self.assertEqual(response, {"detail": "Connection error"})