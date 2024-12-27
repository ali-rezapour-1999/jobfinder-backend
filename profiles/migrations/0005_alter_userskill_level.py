# Generated by Django 5.1.3 on 2024-12-27 06:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userskill_skill_reference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskill',
            name='level',
            field=models.DecimalField(decimal_places=1, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
