# Generated by Django 5.1.3 on 2025-01-15 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userskill_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cv_file',
        ),
    ]
