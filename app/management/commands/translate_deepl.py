"""
This is a Django management command to translate OllamaResponse entries to German using the DeepL API.
# app/management/commands/translate_deepl.py
"""
from django.core.management.base import BaseCommand
from app.models import OllamaResponse
from app.services.deepl_service import translate_to_german
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = "Translate OllamaResponse entries to German using DeepL API."

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

        success_count = 0
        error_count = 0

        for i, response in enumerate(responses, 1):
            self.stdout.write(f"Processing {i}/{responses.count()}: ID {response.id}")
            self.stdout.write(f"Original: {response.response[:100]}...")

            # Call the service to translate the text
            result = translate_to_german(response.response)

            if result["success"]:
                response.response_de = result["corrected_german"]
                response.save()
                self.stdout.write(self.style.SUCCESS(f"✓ Saved: {result['corrected_german'][:100]}..."))
                success_count += 1
            else:
                self.stdout.write(self.style.ERROR(f"✗ Failed to translate response ID {response.id}: {result['error']}"))
                error_count += 1

        self.stdout.write(self.style.SUCCESS(f"Translation complete!"))
        self.stdout.write(self.style.SUCCESS(f"Success: {success_count}, Errors: {error_count}"))