from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page with reset functionality
    path('info/', views.info, name='info'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('result/', views.calculate_result, name='result'), 
    path('recommended-classes/', views.recommended_classes, name='recommended_classes')
]
