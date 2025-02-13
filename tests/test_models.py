from django.test import TestCase
from app.models import Character, BattleOutcome

class CharacterTestCase(TestCase):
    def setUp(self):
        self.hero = Character.objects.create(name="Aragorn", is_main_character=True)
        self.antagonist = Character.objects.create(name="Sauron", is_antagonist=True)

    def test_character_creation(self):
        self.assertEqual(self.hero.name, "Aragorn")
        self.assertTrue(self.hero.is_main_character)
        self.assertFalse(self.hero.is_antagonist)

        self.assertEqual(self.antagonist.name, "Sauron")
        self.assertFalse(self.antagonist.is_main_character)
        self.assertTrue(self.antagonist.is_antagonist)

class BattleOutcomeTestCase(TestCase):
    def setUp(self):
        self.outcome = BattleOutcome.objects.create(player="Aragorn", opponent="Sauron", outcome="Win")

    def test_battle_outcome_creation(self):
        self.assertEqual(self.outcome.player, "Aragorn")
        self.assertEqual(self.outcome.opponent, "Sauron")
        self.assertEqual(self.outcome.outcome, "Win")