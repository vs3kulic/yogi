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
    if "@" not in email:
        return JsonResponse({"error": "Invalid email format."}, status=400)

    # Example subscription logic
    return JsonResponse({"message": "Successfully subscribed!"}, status=200)

def subscribe_email(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    try:
        req = requests.post(
            settings.MAILCHIMP_MEMBERS_ENDPOINT,
            auth=("", settings.MAILCHIMP_API_KEY),
            data=json.dumps(data),
            headers={"Content-Type": "application/json"},
            timeout=5
        )
        try:
            resp_json = req.json()
        except ValueError:
            return 200, {}
        return req.status_code, resp_json

    except requests.ConnectionError:
        return 503, {"detail": "Connection error"}
    except requests.RequestException:
        return 503, {"detail": "Service unavailable."}
