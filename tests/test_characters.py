import unittest
from app.characters import Characters, MainCharacters, AntagonistCharacters

class TestCharacters(unittest.TestCase):
    def test_character_creation(self):
        character = Characters("Hero", "Human", 10, 5, 100, ["For glory!"])
        self.assertEqual(character.name, "Hero")
        self.assertEqual(character.race, "Human")
        self.assertEqual(character.attacks, 10)
        self.assertEqual(character.defense, 5)
        self.assertEqual(character.life_points, 100)
        self.assertEqual(character.quotes, ["For glory!"])

    def test_character_attack(self):
        hero = Characters("Hero", "Human", 10, 5, 100, ["For glory!"])
        villain = Characters("Villain", "Orc", 8, 3, 80, ["You shall fall!"])
        damage = hero.attack(villain)
        self.assertEqual(damage, 7)  # 10 (hero's attack) - 3 (villain's defense)
        self.assertEqual(villain.life_points, 73)  # 80 - 7

    def test_main_character_special_ability(self):
        main_character = MainCharacters("Hero", "Human", 10, 5, 100, ["For glory!"], "Fireball")
        villain = Characters("Villain", "Orc", 8, 3, 80, ["You shall fall!"])
        self.assertEqual(main_character.use_special_ability(villain), "Hero uses Fireball!")
        self.assertEqual(villain.life_points, 80)  # Assuming special ability doesn't affect life points

    def test_antagonist_character_secret_weapon(self):
        antagonist = AntagonistCharacters("Villain", "Orc", 8, 3, 80, ["You shall fall!"], "Poison")
        hero = Characters("Hero", "Human", 10, 5, 100, ["For glory!"])
        self.assertEqual(antagonist.use_secret_weapon(hero), "Villain uses Poison!")
        self.assertEqual(hero.life_points, 100)  # Assuming secret weapon doesn't affect life points

if __name__ == '__main__':
    unittest.main()