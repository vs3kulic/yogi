# Generated by Django 3.2.25 on 2025-05-07 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_image', models.ImageField(upload_to='static/images/')),
            ],
        ),
        migrations.AlterField(
            model_name='yogaclass',
            name='yoga_type',
            field=models.CharField(choices=[('Burnout-Yogini', 'Burnout-Yogini'), ('Ashtanga-Warrior', 'Ashtanga-Warrior'), ('Homeoffice-Yogi', 'Homeoffice-Yogi'), ('Casual-Stretcher', 'Casual-Stretcher')], default='Burnout-Yogini', max_length=50),
        ),
    ]
