import random
from django.db import models
from .utils import fetch_quotes

class Character(models.Model):
    """
    A model class to represent characters in the game.
    """
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100, default="Human")
    attacks = models.IntegerField(default=10)
    defense = models.IntegerField(default=5)
    life_points = models.IntegerField(default=100)
    quotes = models.JSONField(default=list)
    is_main_character = models.BooleanField(default=False)
    is_antagonist = models.BooleanField(default=False)
    special_ability = models.CharField(max_length=100, blank=True, null=True)
    secret_weapon = models.CharField(max_length=100, blank=True, null=True)
    
    objects = models.Manager()

    def __str__(self):
        return str(self.name)

    def attack(self, opponent):
        """
        Attack logic for the characters.

        params: opponent (object) - the opponent character
        return: int - the damage dealt to the opponent
        """
        damage = self.attacks - opponent.defense
        opponent.life_points -= damage
        return damage

    def use_special_ability(self):
        """
        Use the special ability of the main character.
        """
        if self.special_ability:
            return f"{self.name} uses {self.special_ability}!"
        return None

    def use_secret_weapon(self):
        """
        Use the secret weapon of the antagonist character.
        """
        if self.secret_weapon:
            return f"{self.name} uses {self.secret_weapon}!"
        return None

    def fetch_and_assign_quotes(self):
        """
        Fetch and assign a random quote to the main character.
        """
        quotes = fetch_quotes(self.name)
        if quotes and not quotes[0].startswith("Error"):
            self.quotes = [random.choice(quotes)]  # Select one random quote
        else:
            self.quotes = quotes
        self.save()


class BattleOutcome(models.Model):
    """
    A model class to represent the outcome of a battle.
    """
    player = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    outcome = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.player} vs {self.opponent} - {self.outcome} on {self.timestamp}"