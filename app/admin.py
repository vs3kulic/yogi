"""
Description:
    This file is used to register models in the Django admin interface. 
    It allows for easy management of the models through the admin panel.
"""
from django.contrib import admin
from .models import YogaClass

# Register the YogaClass model
admin.site.register(YogaClass)
