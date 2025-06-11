from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

@require_GET
def index(request):
    """
    Home page view.
    """
    return render(request, 'index.html')

@require_GET
def robots_txt(_request):
    """
    Serve the robots.txt file to control web crawler access.
    """
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")