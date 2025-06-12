from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse


class SubscribeViewTests(TestCase):
    """
    This test suite covers the functionality of the subscribe view, including
    successful subscription, missing email, invalid email format, and service
    unavailability.
    """
    def setUp(self):
        self.client = Client()
        self.url = reverse('subscribe')  # Replace 'subscribe' with the actual name of your URL pattern

    @patch('app.views.subscription_views.subscribe_email')  # Fixed path
    def test_subscribe_view_success(self, mock_subscribe_email):
        """
        Test the subscribe view with a valid email address.
        """
        mock_subscribe_email.return_value = (200, {"message": "Successfully subscribed!"})
        response = self.client.post(self.url, {"email": "test@example.com"})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"message": "Successfully subscribed!"})

    def test_subscribe_view_missing_email(self):
        """
        Test the subscribe view with a missing email address.
        """
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"error": "Email is required."})

    def test_subscribe_view_invalid_email(self):
        """
        Test the subscribe view with an invalid email address format.
        """
        response = self.client.post(self.url, {"email": "invalid-email"})
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"error": "Invalid email format."})

    @patch('app.views.subscription_views.subscribe_email')  # Fixed path
    def test_subscribe_view_failure(self, mock_subscribe_email):
        """
        Test the subscribe view with a failure response from the subscription service.
        """
        mock_subscribe_email.return_value = (503, {"detail": "Service unavailable."})
        response = self.client.post(self.url, {"email": "test@example.com"})
        self.assertEqual(response.status_code, 503)
        self.assertJSONEqual(response.content, {"error": "Service unavailable."})
