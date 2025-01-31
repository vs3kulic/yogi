from django.urls import path
from . import views

app_name = 'game'

urlpatterns = [
    path('', views.index, name='index'),
    path('play/', views.play_game, name='play'),
    path('api/select-character/', views.select_character, name='select-character'),
    path('api/select-opponent/', views.select_opponent, name='select-opponent'),
    path('api/run-round/', views.run_round, name='run-round'),
] 