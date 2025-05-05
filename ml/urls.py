from django.urls import path
from .views import artifact_recommendation_view

urlpatterns = [
    path('recommend/', artifact_recommendation_view, name='artifact_recommendation'),
]