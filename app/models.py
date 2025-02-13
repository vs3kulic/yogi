from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    is_main_character = models.BooleanField(default=False)
    is_antagonist = models.BooleanField(default=False)

    objects = models.Manager()

    def __str__(self):
        return self.name


class BattleOutcome(models.Model):
    player = models.CharField(max_length=100)
    opponent = models.CharField(max_length=100)
    outcome = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return f"{self.player} vs {self.opponent} - {self.outcome} on {self.timestamp}"