# Generated by Django 5.2 on 2025-04-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthyfoods',
            name='Ingredients',
            field=models.TextField(max_length=555),
        ),
    ]
