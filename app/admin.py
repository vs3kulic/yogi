"""
Description:

    This file is used to register the Character model in the Django admin interface. 
    It also defines the CharacterAdmin class, which is used to customize the admin interface for the Character model.
"""

from django.contrib import admin
from .models import Character

class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'race', 'attacks', 'defense', 'life_points', 'is_main_character', 'is_antagonist')

    def save_model(self, request, obj, form, change):
        if not change:  # Only assign random attributes when creating a new character
            obj.assign_random_attributes()
        super().save_model(request, obj, form, change)

admin.site.register(Character, CharacterAdmin)