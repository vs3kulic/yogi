from unittest.mock import patch, Mock
import requests
from django.test import TestCase
from app.views.subscription_views import subscribe_email

class SubscribeEmailTests(TestCase):
    """
    This test suite covers the functionality of the subscribe_email function,
    including successful subscription, handling of invalid JSON responses,
    and exceptions during the API call.
    """

    @patch('app.views.subscription_views.requests.post')
    def test_subscribe_email_success(self, mock_post):
        """
        Test subscribe_email with a successful Mailchimp API response.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "abc123"}
        mock_post.return_value = mock_response

        status_code, resp_json = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 200)
        self.assertEqual(resp_json, {"id": "abc123"})

    @patch('app.views.subscription_views.requests.post')
    def test_subscribe_email_failure(self, mock_post):
        """
        Test subscribe_email with a Mailchimp API failure (503 Service Unavailable).
        """
        mock_response = Mock()
        mock_response.status_code = 503
        mock_response.json.return_value = {"detail": "Service unavailable."}
        mock_post.return_value = mock_response

        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 503)
        self.assertEqual(response, {"detail": "Service unavailable."})

    @patch('app.views.subscription_views.requests.post')
    def test_subscribe_email_invalid_json(self, mock_post):
        """
        Test subscribe_email when the Mailchimp API returns invalid JSON.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("Invalid JSON")  # Simulate JSON decode error
        mock_post.return_value = mock_response

        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 200)
        self.assertEqual(response, {})  # Fallback to an empty dictionary

    @patch('app.views.subscription_views.requests.post')
    def test_subscribe_email_exception(self, mock_post):
        """
        Test subscribe_email when a ConnectionError is raised during the API call.
        """
        mock_post.side_effect = requests.exceptions.ConnectionError("Connection error")

        status_code, response = subscribe_email("test@example.com")

        # Assertions
        self.assertEqual(status_code, 503)
        self.assertEqual(response, {"detail": "Connection error"})