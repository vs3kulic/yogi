# Generated by Django 3.2.25 on 2025-05-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_yogaclass_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='OllamaResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prompt', models.TextField()),
                ('response', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionnaireResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('result_type', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
