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
    
    objects = models.Manager()

    def __str__(self):
        return self.name

    def assign_random_attributes(self):
        """
        Assign random values to attacks, defense, and life_points.
        """
        self.attacks = random.randint(5, 15)
        self.defense = random.randint(3, 10)
        self.life_points = random.randint(80, 120)
        self.save()

    def fetch_and_assign_quotes(self):
        try:
            character_id = fetch_character_id(self.name)
            quotes = fetch_quotes(character_id)
            self.quotes = [random.choice(quotes)] if quotes else []
            self.save()
        except Exception as e:
            print(f"Failed to fetch quotes for {self.name}. Error: {str(e)}")

    def attack(self, opponent):
        """
        Perform an attack on an opponent.
        Damage is calculated as the difference between the character's attacks and the opponent's defense (min 0).
        The opponent's life_points are reduced by the damage.
        """
        damage = max(0, self.attacks - opponent.defense)
        opponent.life_points -= damage
        opponent.save()
        return damage


class Artifact(models.Model):
    id = models.AutoField(primary_key=True)  # Enforce a 32-bit signed integer PK
    artifact_name = models.CharField(max_length=100)
    offensive_property = models.IntegerField(default=0)
    defensive_property = models.IntegerField(default=0)
    character = models.ForeignKey(
        'Character',
        on_delete=models.CASCADE,
        related_name='artifacts'
    )
    objects = models.Manager()

    def __str__(self):
        return self.artifact_name

    class Meta:
        db_table = 'app_artifacts'


class BattleOutcome(models.Model):
    player = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    outcome = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    main_artifact = models.ForeignKey(
        'Artifact',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='battle_main'
    )
    opponent_artifact = models.ForeignKey(
        'Artifact',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='battle_opponent'
    )
    objects = models.Manager()