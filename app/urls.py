"""This module defines the URL patterns for the application.
It includes paths for the home page, admin panel, questionnaire, result calculation,
robots.txt, sitemap, subscription view and the sitemap for static views.
"""
from django.urls import path
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from app.views.static_views import index, robots_txt  # Correct import for static views
from app.views.questionnaire_views import questionnaire  # Correct import for questionnaire views
from app.views.result_views import calculate_result  # Import from result_views.py
from app.views.subscription_views import subscribe_view  # Correct import for subscription view
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', index, name='index'),  # Home page
    path('admin/', admin.site.urls),  # Admin panel
    path('questionnaire/', questionnaire, name='questionnaire'),  # Questionnaire view
    path('robots.txt', robots_txt, name='robots_txt'),  # Robots.txt view
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('result/', calculate_result, name='result'),  # Result view
    path('subscribe/', subscribe_view, name='subscribe'),  # Subscription view
]
