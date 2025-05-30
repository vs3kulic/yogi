from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, Adjust
from django.db import models

class YogaClass(models.Model):
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
    original_image = models.ImageField(upload_to='static/images/')
    optimized_image = ImageSpecField(
        source='original_image',
        processors=[ResizeToFit(800, 800), Adjust(contrast=1.2, sharpness=1.1)],
        format='PNG',
        options={'quality': 80}
    )

class QuestionnaireResult(models.Model):
    user_id = models.CharField(max_length=255, null=True, blank=True)  # Optional user identifier
    result_type = models.CharField(max_length=255)  # e.g., "Ashtanga-Warrior"
    created_at = models.DateTimeField(auto_now_add=True)

class OllamaResponse(models.Model):
    prompt = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

