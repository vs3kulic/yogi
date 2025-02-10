# Text-based Fellowship of the Ring game
import sys
import os

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Fellowships.game import Game

game = Game()
player = game.select_character(1)  # Example: selecting the first character
opponent = game.select_opponent()
scores = game.run_round(player, opponent)
result = game.declare_winner(scores)
print(result)