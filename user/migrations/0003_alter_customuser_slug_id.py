# Generated by Django 5.1.3 on 2025-02-07 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_slug_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='slug_id',
            field=models.SlugField(blank=True, default='1b47fa59', max_length=8, unique=True),
        ),
    ]
