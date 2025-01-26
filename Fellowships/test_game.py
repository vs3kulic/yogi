import unittest
from characters import Characters, MainCharacters, AntagonistCharacters

class TestCharacters(unittest.TestCase):
    def test_characters(self):
        character = Characters("Aragorn", "Human", 15, 10, 120, ["For Gondor!"])
        self.assertEqual(character.name, "Aragorn")
        self.assertEqual(character.race, "Human")
                         
    def test_main_characters(self):
        main_character = MainCharacters("Aragorn", "Human", 15, 10, 120, ["For Gondor!"], "Andúril Strike")
        self.assertEqual(main_character.name, "Aragorn")
        self.assertEqual(main_character.special_ability, "Andúril Strike")  

    def test_antagonist_characters(self):
        antagonist = AntagonistCharacters("Sauron", "Maia", 20, 15, 200, ["I see you!"], "Dark Flame")
        self.assertEqual(antagonist.name, "Sauron")
        self.assertEqual(antagonist.secret_weapon, "Dark Flame")

if __name__ == '__main__':
    unittest.main()