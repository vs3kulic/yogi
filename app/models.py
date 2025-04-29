from django.db import models

class YogaClass(models.Model):
    TYPE_CHOICES = [
        ('Burnout-Yogini', 'Burnout-Yogini'),
        ('Ashtanga-Warrior', 'Ashtanga-Warrior'),
        ('Homeoffice-Yogi', 'Homeoffice-Yogi'),
        ('Casual-Stretcher', 'Casual-Stretcher'),
        ('Cross-Type', 'Cross-Type'),
    ]

    yoga_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='Burnout-Yogini')
    name = models.CharField(max_length=255)
    class_type = models.CharField(max_length=50, default="Regular")
    key_features = models.TextField(null=True, blank=True)
    ideal_for = models.TextField()
    ideal_for_short = models.CharField(max_length=50, null=True, blank=True)  # Add this field

    def __str__(self):
        return self.name