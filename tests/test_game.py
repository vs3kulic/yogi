import unittest
from app.characters import Characters, MainCharacters, AntagonistCharacters
from django.test import TestCase
from app.game import Game, GameCharacter

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

class GameTestCase(TestCase):
    def setUp(self):
        self.player = GameCharacter("Aragorn", 100, 10)
        self.opponent = GameCharacter("Sauron", 100, 10)
        self.game = Game()

    def test_coin_toss(self):
        result = self.game.coin_toss("heads")
        self.assertIn(result, [True, False])

    def test_run_round(self):
        player_life, opponent_life, steps = self.game.run_round(self.player, self.opponent)
        self.assertTrue(player_life >= 0)
        self.assertTrue(opponent_life >= 0)
        self.assertTrue(len(steps) > 0)

    def test_declare_winner(self):
        scores = (self.player.life_points, self.opponent.life_points, [])
        result = self.game.declare_winner(scores)
        self.assertIn(result, ["Player wins!", "Opponent wins!", "It's a tie!"])

if __name__ == '__main__':
    unittest.main()