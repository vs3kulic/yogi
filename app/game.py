import random
from .models import Character

class Game:
    """
    A class to represent the game.
    """
    def __init__(self):
        self.main_characters = Character.objects.filter(is_main_character=True)
        self.antagonists = Character.objects.filter(is_antagonist=True)

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
        Toss a coin and return the result.

        params: user_choice (str) - the user's choice for the coin toss
        return: bool - True if the user wins, False otherwise
        """
        coin_result = random.choice(["heads", "tails"])
        return user_choice == coin_result

    def run_round(self, player, opponent):
        """
        Run a round of the game between the player and the opponent.

        params: player (object) - the player character
                opponent (object) - the opponent character
        return: tuple - the scores of the player, the opponent and the steps of the game
        """
        steps = []
        player_turn = self.coin_toss("heads")  # Example: player always chooses heads for simplicity
        
        while player.life_points > 0 and opponent.life_points > 0:
            if player_turn:
                damage = player.attack(opponent)
                steps.append(f"{player.name} attacks {opponent.name} for {damage} damage!")
                steps.append(f"{opponent.name} has {opponent.life_points} life points left.")
            else:
                damage = opponent.attack(player)
                steps.append(f"{opponent.name} attacks {player.name} for {damage} damage!")
                steps.append(f"{player.name} has {player.life_points} life points left.")
            player_turn = not player_turn
        
        return player.life_points, opponent.life_points, steps

    def declare_winner(self, scores):
        """
        Declare the winner based on the scores of the player and the opponent.

        params: scores (tuple) - the scores of the player and the opponent
        return: str - the result of the game
        """
        player_life_points, opponent_life_points, _ = scores
        if player_life_points > opponent_life_points:
            return "Player wins!"
        elif player_life_points < opponent_life_points:
            return "Opponent wins!"
        else:
            return "It's a tie!"
