from unittest.mock import patch
import requests
from django.test import TestCase
from app.views import subscribe_email

class SubscribeEmailTests(TestCase):
    """
    This test suite covers the functionality of the subscribe_email function,
    including successful subscription, handling of invalid JSON responses,
    and exceptions during the API call.
    """

    @patch('requests.post')  # Mock the requests.post method
    def test_subscribe_email_success(self, mock_post):
        """
        Test subscribe_email with a successful Mailchimp API response.
        """
        # Mock the API response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"message": "Successfully subscribed!"}

        # Call the function
        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 200)
        self.assertEqual(response, {"message": "Successfully subscribed!"})

    @patch('requests.post')
    def test_subscribe_email_failure(self, mock_post):
        """
        Test subscribe_email with a Mailchimp API failure (503 Service Unavailable).
        """
        # Mock the API response
        mock_post.return_value.status_code = 503
        mock_post.return_value.json.return_value = {"detail": "Service unavailable."}

        # Call the function
        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 503)
        self.assertEqual(response, {"detail": "Service unavailable."})

    @patch('requests.post')
    def test_subscribe_email_invalid_json(self, mock_post):
        """
        Test subscribe_email when the Mailchimp API returns invalid JSON.
        """
        # Mock the API response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.side_effect = ValueError  # Simulate invalid JSON

        # Call the function
        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 200)
        self.assertEqual(response, {})  # Fallback to an empty dictionary

    @patch('requests.post', side_effect=requests.exceptions.ConnectionError("Connection error"))
    def test_subscribe_email_exception(self, mock_post):
        """
        Test subscribe_email when a ConnectionError is raised during the API call.
        """
        # Call the function
        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 503)
        self.assertEqual(response, {"detail": "Connection error"})