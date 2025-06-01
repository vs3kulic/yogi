from django.core.management.base import BaseCommand
from app.models import OllamaResponse
from app.services.deepl_service import translate_to_german, fix_german_text
import time

class Command(BaseCommand):
    help = "Fix Ollama responses using DeepL translation service"

    def add_arguments(self, parser):
        parser.add_argument(
            '--method',
            type=str,
            choices=['translate', 'fix'],
            default='translate',
            help='Method to use: translate (DE->EN->DE) or fix (DE->DE)'
        )
        parser.add_argument(
            '--limit',
            type=int,
            default=None,
            help='Limit number of responses to process'
        )
        parser.add_argument(
            '--force',
            action='store_true',
            help='Force re-processing of already processed responses'
        )

    def handle(self, *args, **options):
        method = options['method']
        limit = options['limit']
        force = options['force']

        # Get responses that need processing
        if force:
            queryset = OllamaResponse.objects.all()
        else:
            queryset = OllamaResponse.objects.filter(response_de__isnull=True)

        if limit:
            queryset = queryset[:limit]

        total_count = queryset.count()
        self.stdout.write(self.style.SUCCESS(f"Processing {total_count} responses using method: {method}"))

        success_count = 0
        error_count = 0

        for i, ollama_response in enumerate(queryset, 1):
            self.stdout.write(f"Processing {i}/{total_count}: ID {ollama_response.id}")
            
            # Show original response
            self.stdout.write(f"Original: {ollama_response.response[:100]}...")

            # Choose processing method
            if method == 'translate':
                result = translate_to_german(ollama_response.response)
            else:  # fix
                result = fix_german_text(ollama_response.response)

            if result['success']:
                # Save the corrected German
                ollama_response.response_de = result['corrected_german']
                ollama_response.save()
                
                self.stdout.write(self.style.SUCCESS(f"✓ Fixed: {result['corrected_german'][:100]}..."))
                success_count += 1
            else:
                self.stdout.write(self.style.ERROR(f"✗ Error: {result['error']}"))
                error_count += 1

            # Rate limiting to avoid hitting DeepL API limits
            if i % 10 == 0:  # Pause every 10 requests
                self.stdout.write("Pausing for rate limiting...")
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS(f"Processing complete!"))
        self.stdout.write(self.style.SUCCESS(f"Successfully processed: {success_count}"))
        self.stdout.write(self.style.ERROR(f"Errors: {error_count}"))