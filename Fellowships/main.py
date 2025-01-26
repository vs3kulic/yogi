# Text-based Fellowship of the Ring game
from game import Game

player = Game().select_character()
opponent = Game().select_opponent()
run_round = Game().run_round(player, opponent) 
declare_winner = Game().declare_winner(run_round)