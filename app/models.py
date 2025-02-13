from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100, default="Human")  # Add race field
    attacks = models.IntegerField(default=10)  # Add attacks field
    defense = models.IntegerField(default=5)  # Add defense field
    life_points = models.IntegerField(default=100)  # Add life_points field
    quotes = models.JSONField(default=list)  # Add quotes field
    is_main_character = models.BooleanField(default=False)
    is_antagonist = models.BooleanField(default=False)
    special_ability = models.CharField(max_length=100, blank=True, null=True)  # Add special_ability field
    secret_weapon = models.CharField(max_length=100, blank=True, null=True)  # Add secret_weapon field
    
    objects = models.Manager()

    def __str__(self):
        return self.name

    def attack(self, opponent):
        damage = self.attacks - opponent.defense
        opponent.life_points -= damage
        return damage

    def use_special_ability(self, opponent):
        if self.special_ability:
            return f"{self.name} uses {self.special_ability}!"
        return None

    def use_secret_weapon(self, opponent):
        if self.secret_weapon:
            return f"{self.name} uses {self.secret_weapon}!"
        return None


class BattleOutcome(models.Model):
    player = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    outcome = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.player} vs {self.opponent} - {self.outcome} on {self.timestamp}"