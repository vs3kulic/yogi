from django.test import TestCase, Client
from django.urls import reverse
from app.models import Character, BattleOutcome

class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.hero = Character.objects.create(name="Aragorn", is_main_character=True)
        self.antagonist = Character.objects.create(name="Sauron", is_antagonist=True)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.hero.name)

    def test_select_character_view(self):
        response = self.client.post(reverse('select_character'), {'character_id': self.hero.id})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'select_character.html')
        self.assertContains(response, f"You picked {self.hero.name} as your fighter!")

    def test_opponent_selected_view(self):
        session = self.client.session
        session['selected_hero'] = self.hero.name
        session.save()
        response = self.client.get(reverse('opponent_selected'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'opponent_selected.html')
        self.assertContains(response, f"Your opponent is {self.antagonist.name}")

    def test_coin_toss_view_get(self):
        response = self.client.get(reverse('coin_toss'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coin_toss.html')

    def test_coin_toss_view_post(self):
        response = self.client.post(reverse('coin_toss'), {'coin_choice': 'heads'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coin_toss_result.html')
        self.assertIn('coin_result', response.context)

    def test_battle_view(self):
        session = self.client.session
        session['selected_hero'] = self.hero.name
        session['opponent'] = self.antagonist.name
        session.save()
        response = self.client.get(reverse('battle'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'battle.html')
        self.assertIn('result', response.context)
        self.assertIn('steps', response.context)

    def test_battle_results_view(self):
        session = self.client.session
        session['selected_hero'] = self.hero.name
        session.save()
        BattleOutcome.objects.create(player=self.hero.name, opponent=self.antagonist.name, outcome="Win")
        response = self.client.get(reverse('battle_results'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'battle_results.html')
        self.assertContains(response, self.hero.name)
        self.assertContains(response, self.antagonist.name)