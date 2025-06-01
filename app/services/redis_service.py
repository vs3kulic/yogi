from django.core.cache import cache
from app.models import OllamaResponse

def load_responses_to_cache():
    responses = OllamaResponse.objects.all()
    for response in responses:
        cache_key = f"ollama_response_{response.prompt.split(' ')[-1].strip()}"
        cache.set(cache_key, response.response, timeout=None)
        print(f"Cached: {cache_key} -> {response.response}")

# Run this in a Django shell
# python manage.py shell
#
# from app.services.cache_loader import load_responses_to_cache
# load_responses_to_cache()
