from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust
from django.db import models

class YogaClass(models.Model):
    """Model representing a type of yoga class with various attributes."""
    
    TYPE_CHOICES = [
        ('Burnout-Yogini', 'Burnout-Yogini'),
        ('Ashtanga-Warrior', 'Ashtanga-Warrior'),
        ('Homeoffice-Yogini', 'Homeoffice-Yogini'),
        ('Casual-Stretcher', 'Casual-Stretcher')
    ]

    yoga_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Burnout-Yogini')
    name = models.CharField(max_length=255)
    class_type = models.CharField(max_length=50, default="Regular")
    key_features = models.TextField(null=True, blank=True)
    ideal_for = models.TextField()
    ideal_for_short = models.CharField(max_length=50, null=True, blank=True)  # Add this field
    description = models.TextField(default="Default description")  # Add this field

    def __str__(self):
        return self.name

class MyImageModel(models.Model):
    """Model for storing images with optimized versions."""
    
    original_image = models.ImageField(upload_to='static/images/')
    optimized_image = ImageSpecField(
        source='original_image',
        processors=[ResizeToFit(800, 800), Adjust(contrast=1.2, sharpness=1.1)],
        format='PNG',
        options={'quality': 80}
    )

class QuestionnaireResult(models.Model):
    """Model to store results of a questionnaire."""
    
    session_id = models.CharField(max_length=255, unique=True, null=True, blank=True)  # Allow null values
    answers = models.JSONField(default=dict)  # Set default to an empty dictionary
    result_type = models.CharField(max_length=255)  # e.g., "Ashtanga-Warrior"
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the result was created

    def __str__(self):
        return f"Result: {self.result_type} (Created at: {self.created_at})"

class OllamaResponse(models.Model):
    """Model to store responses from the Ollama API."""
    
    prompt = models.TextField()
    response = models.TextField()
    combinations = models.JSONField(null=True, blank=True)  # New field to store answer combinations
    response_de = models.TextField(null=True, blank=True)  # Translated response in German
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"OllamaResponse (Created at: {self.created_at})"

