from django.urls import path
from . import views
from .views import artifact_selection, artifact_selected, battle

urlpatterns = [
    path('', views.index, name='index'),
    path('character/<int:character_id>/', views.select_character, name='select_character'),
    path('opponent_selected/', views.opponent_selected, name='opponent_selected'),
    path('coin_toss/', views.coin_toss, name='coin_toss'), 
    path('coin_toss_result/<str:result>/', views.coin_toss_result, name='coin_toss_result'),
    path('battle/', battle, name='battle'),
    path('battle_results/', views.battle_results, name='battle_results'),
    path('artifact-selection/', artifact_selection, name='artifact_selection'),
    path('artifact-selected/', artifact_selected, name='artifact_selected'),
    path('next-step/', battle, name='next_step'),
    path('opponent-artifact/', views.opponent_artifact, name='opponent_artifact'),
]