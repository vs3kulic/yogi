import json
import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["POST"])
def subscribe_view(request):
    """
    Handles email subscription.
    """
    email = request.POST.get("email")
    if not email:
        return JsonResponse({"error": "Email is required."}, status=400)

    # Example subscription logic
    return JsonResponse({"message": "Successfully subscribed!"}, status=200)

def subscribe_email(email):
    """
    Helper function to subscribe an email address to Mailchimp.
    """
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    try:
        # Send a POST request to Mailchimp API
        req = requests.post(
            settings.MAILCHIMP_MEMBERS_ENDPOINT,
            auth=("", settings.MAILCHIMP_API_KEY),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        try:
            resp_json = req.json()  # Attempt to decode JSON response
        except ValueError:
            resp_json = {}  # Fallback to empty dict if JSON decoding fails
        
        return req.status_code, resp_json

    except requests.RequestException as e:
        # Handle request-related exceptions (e.g., connection errors, timeouts)
        return 503, {"detail": str(e)}
