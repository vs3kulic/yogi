from django.core.management.base import BaseCommand
from app.models import QuestionnaireResult, OllamaResponse
from app.services.ollama_service import call_ollama
from app.views import clean_text
import random

class Command(BaseCommand):
    help = "Generate 1,000 Ollama responses based on random questionnaire results."

    def handle(self, *args, **kwargs):
        results = QuestionnaireResult.objects.all()
        if not results.exists():
            self.stdout.write(self.style.ERROR("No questionnaire results found."))
            return

        for _ in range(1000):
            random_result = random.choice(results)
            prompt = f"Based on the yoga type '{random_result.result_type}', provide a personalized yoga tip in Markdown format. Limit to 20 words."
            ollama_response = call_ollama(prompt)

            if "error" not in ollama_response:
                raw_text = ollama_response.get("response", "No response received.")
                cleaned_text = clean_text(raw_text)
                OllamaResponse.objects.create(prompt=prompt, response=cleaned_text)

        self.stdout.write(self.style.SUCCESS("Successfully generated 1,000 Ollama responses."))