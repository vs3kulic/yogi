# Generated by Django 3.2.25 on 2025-05-31 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_ollamaresponse_combinations'),
    ]

    operations = [
        migrations.AddField(
            model_name='ollamaresponse',
            name='response_de',
            field=models.TextField(blank=True, null=True),
        ),
    ]
