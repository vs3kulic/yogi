import random
from django.db import models
from .utils import fetch_quotes, fetch_character_id

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

    def assign_random_attributes(self):
        """
        Assign random values to attacks, defense, and life_points.
        """
        self.attacks = random.randint(5, 15)
        self.defense = random.randint(3, 10)
        self.life_points = random.randint(80, 120)
        self.save()

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
        if self.special_ability:
            return f"{self.name} uses {self.special_ability}!"
        return None

    def use_secret_weapon(self):
        if self.secret_weapon:
            return f"{self.name} uses {self.secret_weapon}!"
        return None

    def fetch_and_assign_quotes(self):
        try:
            character_id = fetch_character_id(self.name)
            quotes = fetch_quotes(character_id)
            self.quotes = [random.choice(quotes)] if quotes else []
            self.save()
        except Exception as e:
            print(f"Failed to fetch quotes for {self.name}. Error: {str(e)}")


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