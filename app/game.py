import random
from .game_data import main_characters, antagonists

class Game:
    """
    A class to represent the game.
    """
    def __init__(self):
        self.main_characters = main_characters
        self.antagonists = antagonists

    def select_character(self, choice):
        """
        Select a character from the list of main characters.
        """
        if 0 <= choice < len(self.main_characters):
            fighter = self.main_characters[choice]
            return fighter
        else:
            return None
    
    def select_opponent(self):
        """
        Select an opponent from the list of antagonists.
        """
        opponent = random.choice(self.antagonists)
        return opponent

    def coin_toss(self, user_choice):
        """
        Simulate a coin toss and compare the result with the user's choice.
        """
        coin = random.choice(["heads", "tails"])
        return user_choice == coin

    def run_round(self, player, opponent):
        """
        Simulate a round of the game between the player and the opponent.
        """
        player_turn = self.coin_toss("heads")  # Example: player always chooses heads for simplicity
        
        while player.life_points > 0 and opponent.life_points > 0: 
            if player_turn:
                damage = player.attack(opponent)
                print(f"{player.name} attacks {opponent.name} for {damage} damage!")
                print(f"{opponent.name} has {opponent.life_points} life points left.")
            else:
                damage = opponent.attack(player)
                print(f"{opponent.name} attacks {player.name} for {damage} damage!")
                print(f"{player.name} has {player.life_points} life points left.")
            player_turn = not player_turn
        
        return player.life_points, opponent.life_points

    def declare_winner(self, scores):
        """
        Declare the winner based on the scores of the player and the opponent.
        """
        player_life_points, opponent_life_points = scores
        if player_life_points > opponent_life_points:
            return "Player wins!"
        elif player_life_points < opponent_life_points:
            return "Opponent wins!"
        else:
            return "It's a tie!"