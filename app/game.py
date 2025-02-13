import random
from .models import Character

class GameCharacter:
    def __init__(self, name, life_points, attack_points):
        self.name = name
        self.life_points = life_points
        self.attack_points = attack_points

    def attack(self, opponent):
        damage = self.attack_points
        opponent.life_points -= damage
        return damage

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
        return user_choice == "heads"

    def run_round(self, player, opponent):
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
        """
        player_life_points, opponent_life_points, _ = scores
        if player_life_points > opponent_life_points:
            return "Player wins!"
        elif player_life_points < opponent_life_points:
            return "Opponent wins!"
        else:
            return "It's a tie!"