# Characters class for the game

class Characters:
    def __init__(self, name, race, attacks, defense, life_points, quotes):
        self.name = name
        self.race = race
        self.attacks = attacks
        self.defense = defense
        self.life_points = life_points
        self.quotes = quotes
    
    def attack(self, opponent): 
        damage = self.attacks - opponent.defense
        opponent.life_points -= damage 
        return damage 
    
class MainCharacters(Characters):
    def __init__(self, name, race, attacks, defense, life_points, quotes, special_ability):
        super().__init__(name, race, attacks, defense, life_points, quotes)
        self.special_ability = special_ability

    def use_special_ability(self, opponent):
        damage = self.attacks * 2 - opponent.defense
        opponent.life_points -= damage
        return f"{self.name} uses {self.special_ability}!"
    
class AntagonistCharacters(Characters):
    def __init__(self, name, race, attacks, defense, life_points, quotes, secret_weapon):
        super().__init__(name, race, attacks, defense, life_points, quotes)
        self.secret_weapon = secret_weapon

    def use_secret_weapon(self, opponent):
        damage = self.attacks * 2 - opponent.defense
        opponent.life_points -= damage
        return f"{self.name} uses {self.secret_weapon}!" 