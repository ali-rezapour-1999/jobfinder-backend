# Generated by Django 5.1.3 on 2025-01-16 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0006_remove_profile_phone_number_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="slug_id",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="username",
        ),
    ]
