from django.db import models

class YogaClass(models.Model):
    TYPE_CHOICES = [
        ('A', 'Burnout-Yogini'),
        ('B', 'Ashtanga-Warrior'),
        ('C', 'Homeoffice-Yogi'),
        ('D', 'Casual-Stretcher'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    def __str__(self):
        return self.name