# Generated by Django 3.2.25 on 2025-04-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YogaClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yoga_type', models.CharField(choices=[('Burnout-Yogini', 'Burnout-Yogini'), ('Ashtanga-Warrior', 'Ashtanga-Warrior'), ('Homeoffice-Yogi', 'Homeoffice-Yogi'), ('Casual-Stretcher', 'Casual-Stretcher'), ('Cross-Type', 'Cross-Type')], default='Burnout-Yogini', max_length=50)),
                ('name', models.CharField(max_length=255)),
                ('class_type', models.CharField(default='Regular', max_length=50)),
                ('key_features', models.TextField(blank=True, null=True)),
                ('ideal_for', models.TextField()),
                ('ideal_for_short', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
