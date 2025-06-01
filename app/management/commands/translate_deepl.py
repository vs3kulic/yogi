"""
This is a Django management command to translate OllamaResponse entries to German using the DeepL API.
# app/management/commands/translate_deepl.py
"""

from django.core.management.base import BaseCommand
from app.models import OllamaResponse
from django.conf import settings
import requests
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Translate OllamaResponse entries to German using DeepL API."

    def translate_to_german(self, text):
        """
        Translates the given text to German using DeepL API.
        """
        api_url = "https://api-free.deepl.com/v2/translate"  # Use the correct endpoint
        api_key = settings.DEEPL_API_KEY  # Load the API key from settings
        data = {
            "auth_key": api_key,
            "text": text,
            "target_lang": "DE"
        }
        try:
            logger.info(f"Sending request to DeepL API: {api_url}")
            response = requests.post(api_url, data=data)
            logger.info(f"Response status code: {response.status_code}")
            logger.info(f"Response text: {response.text}")

            if response.status_code == 200:
                return response.json().get("translations", [{}])[0].get("text", "")
            else:
                logger.error(f"DeepL API error: {response.status_code} - {response.text}")
                return None
        except requests.RequestException as e:
            logger.error(f"Error connecting to DeepL API: {str(e)}")
            return None

    def handle(self, *args, **kwargs):
        """
        Fetch responses from OllamaResponse, translate them to German, and save the translations.
        """
        # Fetch all entries where response_de is null
        responses = OllamaResponse.objects.filter(response_de__isnull=True)

        if not responses.exists():
            self.stdout.write(self.style.SUCCESS("No entries to translate."))
            return

        self.stdout.write(self.style.SUCCESS(f"Found {responses.count()} entries to translate."))

        for response in responses:
            self.stdout.write(f"Translating response ID {response.id}...")
            translated_text = self.translate_to_german(response.response)
            if translated_text:
                response.response_de = translated_text
                response.save()
                self.stdout.write(self.style.SUCCESS(f"Translated and saved response ID {response.id}."))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to translate response ID {response.id}."))