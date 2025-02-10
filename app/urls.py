from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select_character/', views.select_character, name='select_character'),
    path('opponent_selected/', views.opponent_selected, name='opponent_selected'),
    path('coin_toss/', views.coin_toss, name='coin_toss'),
    path('battle/', views.battle, name='battle')
]