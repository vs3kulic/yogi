import requests
import os
from django.conf import settings

DEEPL_API_URL = "https://api.deepl.com/v2/translate"  # Use the Pro endpoint

def get_deepl_api_key():
    """Get DeepL API key from settings or environment variable."""
    api_key = getattr(settings, 'DEEPL_API_KEY', None) or os.getenv('DEEPL_API_KEY')
    if not api_key:
        raise ValueError("DeepL API key not found. Set DEEPL_API_KEY in settings or environment.")
    return api_key

def translate_to_german(text, source_lang="DE", target_lang="DE"):
    """
    Translates the given text using DeepL API.
    For German text correction, we translate DE->EN->DE to improve quality.
    """
    api_key = get_deepl_api_key()

    headers = {
        "Authorization": f"DeepL-Auth-Key {api_key}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    try:
        # Step 1: DE -> EN (clean up the text)
        data_en = {
            "text": text,
            "source_lang": source_lang,
            "target_lang": "EN",
        }
        response_en = requests.post(DEEPL_API_URL, headers=headers, data=data_en)
        response_en.raise_for_status()
        english_text = response_en.json()["translations"][0]["text"]

        # Step 2: EN -> DE (translate back to clean German)
        data_de = {
            "text": english_text,
            "source_lang": "EN",
            "target_lang": target_lang,
            "formality": "less",  # Use less formal language
        }
        response_de = requests.post(DEEPL_API_URL, headers=headers, data=data_de)
        response_de.raise_for_status()
        german_text = response_de.json()["translations"][0]["text"]

        return {
            "success": True,
            "original": text,
            "english": english_text,
            "corrected_german": german_text,
        }

    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "error": f"DeepL API error: {str(e)}",
            "original": text,
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Unexpected error: {str(e)}",
            "original": text,
        }

def fix_german_text(text):
    """
    Simplified function that just tries to fix German text directly.
    """
    if not DEEPL_API_KEY:
        raise ValueError("DeepL API key not found. Set DEEPL_API_KEY in settings or environment.")
    
    try:
        headers = {
            "Authorization": f"DeepL-Auth-Key {DEEPL_API_KEY}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        
        # Translate DE to DE (DeepL will clean up the text)
        data = {
            "text": text,
            "source_lang": "DE",
            "target_lang": "DE",
        }
        
        response = requests.post(DEEPL_API_URL, headers=headers, data=data)
        response.raise_for_status()
        
        fixed_text = response.json()["translations"][0]["text"]
        
        return {
            "success": True,
            "original": text,
            "corrected_german": fixed_text
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "original": text
        }