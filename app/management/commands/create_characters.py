from django.core.management.base import BaseCommand
from app.models import Character

class Command(BaseCommand):
    help = 'Create characters with random attributes'

    def handle(self, *args, **kwargs):
        characters = [
            {"name": "Aragorn", "race": "Human", "is_main_character": True},
            {"name": "Frodo", "race": "Hobbit", "is_main_character": True},
            {"name": "Legolas", "race": "Elf", "is_main_character": True},
            {"name": "Gimli", "race": "Dwarf", "is_main_character": True},
            {"name": "Gandalf", "race": "Wizard", "is_main_character": True},
            {"name": "Sauron", "race": "Maia", "is_antagonist": True},
            {"name": "Saruman", "race": "Wizard", "is_antagonist": True},
            {"name": "Gollum", "race": "Hobbit", "is_antagonist": True},
            {"name": "Nazgul", "race": "Wraith", "is_antagonist": True},
            {"name": "Lurtz", "race": "Uruk-hai", "is_antagonist": True},
        ]

        for char_data in characters:
            try:
                character = Character(**char_data)
                character.assign_random_attributes()
                character.save()
                print(f"Created character: {character.name}")
            except Exception as e:
                print(f"Failed to create character: {char_data['name']}. Error: {str(e)}")