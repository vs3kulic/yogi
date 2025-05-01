from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page with reset functionality
    path('info/', views.info, name='info'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('calculate_result/', views.calculate_result, name='calculate_result'),
    path('recommended_classes/', views.recommended_classes, name='recommended_classes'),
    path('subscribe/', views.subscribe_view, name='subscribe')
]
