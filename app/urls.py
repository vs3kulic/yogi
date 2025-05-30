from django.urls import path
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.index, name='index'),  # Home page with reset functionality
    path('admin/', admin.site.urls),  # Admin panel URL
    path('info/', views.info, name='info'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('calculate_result/', views.calculate_result, name='calculate_result'),
    path('recommended_classes/', views.recommended_classes, name='recommended_classes'),
    path('subscribe/', views.subscribe_view, name='subscribe'),
    path('robots.txt', views.robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('result/', views.result, name='result'),
    path('api/yoga-classes/', views.yoga_classes_api, name='yoga_classes_api'),
    path("ollama-test/", views.ollama_test_view, name="ollama_test"),
]
