# Generated by Django 5.1.3 on 2025-01-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdeviceinfo',
            name='screen_resolution',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userdeviceinfo',
            name='timezone',
            field=models.TextField(blank=True, null=True),
        ),
    ]
