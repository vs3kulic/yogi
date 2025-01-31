# Text-based Fellowship of the Ring game
from Fellowships.game import Game

game = Game()
player = game.select_character(1)  # Example: selecting the first character
opponent = game.select_opponent()
run_round = game.run_round(player, opponent) 
declare_winner = game.declare_winner(run_round)