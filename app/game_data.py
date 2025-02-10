#!/usr/bin/env python
import os
import sys

from app.characters import MainCharacters, AntagonistCharacters

main_characters = [
    MainCharacters("Aragorn", "Human", 15, 10, 90, ["For Gondor!"], "Andúril Strike"),
    MainCharacters("Legolas", "Elf", 20, 10, 150, ["For the Elves!"], "Arrow Barrage"),
    MainCharacters("Gimli", "Dwarf", 15, 20, 120, ["For the Dwarves!"], "Axe Fury"),
    MainCharacters("Gandalf", "Wizard", 20, 5, 130, ["You shall not pass!"], "Lightning Bolt"),
    MainCharacters("Frodo", "Hobbit", 5, 5, 80, ["For the Shire!"], "Sting Strike")
]

antagonists = [
    AntagonistCharacters("Sauron", "Maia", 20, 10, 140, ["I see you!"], "Dark Flame"),
    AntagonistCharacters("Saruman", "Wizard", 20, 5, 130, ["Against the free peoples!"], "Staff Strike"),
    AntagonistCharacters("Nazgûl", "Human", 15, 10, 90, ["No man can kill me!"], "Morgul Blade"),
    AntagonistCharacters("Lurtz", "Uruk-hai", 20, 15, 90, ["Find the halflings!"], "Brutal Slash"),
    AntagonistCharacters("Gollum", "Hobbit", 5, 5, 80, ["My precious!"], "Sneak Attack")
]

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)