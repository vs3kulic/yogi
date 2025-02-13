import random
from .utils import fetch_quotes

# Characters class for the game

class Characters:
    """
    A class to represent characters in the game.
    """
    def __init__(self, name, race, attacks, defense, life_points, quotes):
        """
        Constructor for the Characters class.
        """
        self.name = name
        self.race = race
        self.attacks = attacks
        self.defense = defense
        self.life_points = life_points
        self.quotes = quotes

    def attack(self, opponent):
        """
        Attack logic for the characters.

        params: opponent (object) - the opponent character
        return: int - the damage dealt to the opponent
        """
        damage = self.attacks - opponent.defense
        opponent.life_points -= damage
        return damage

class MainCharacters(Characters):
    """
    A class to represent main characters in the game.
    """
    def __init__(self, name, race, attacks, defense, life_points, quotes, special_ability):
        super().__init__(name, race, attacks, defense, life_points, quotes)
        self.special_ability = special_ability

    def use_special_ability(self):
        """
        Use the special ability of the main character.

        params: None
        return: str - the special ability used by the main character
        """
        return f"{self.name} uses {self.special_ability}!"

    def fetch_and_assign_quotes(self):
        """
        Fetch and assign a random quote to the main character.

        params: None
        return: None
        """
        quotes = fetch_quotes(self.name)
        if quotes and not quotes[0].startswith("Error"):
            self.quotes = [random.choice(quotes)]  # Select one random quote
        else:
            self.quotes = quotes

class AntagonistCharacters(Characters):
    """
    A class to represent antagonist characters in the game.
    """
    def __init__(self, name, race, attacks, defense, life_points, quotes, secret_weapon):
        """
        Constructor for the AntagonistCharacters class.
        """
        super().__init__(name, race, attacks, defense, life_points, quotes)
        self.secret_weapon = secret_weapon

    def use_secret_weapon(self):
        """
        Use the secret weapon of the antagonist character.

        params: None
        return: str - the secret weapon used by the antagonist
        """
        return f"{self.name} uses {self.secret_weapon}!"