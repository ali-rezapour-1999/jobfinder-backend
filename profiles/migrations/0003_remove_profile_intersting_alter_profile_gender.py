# Generated by Django 5.1.3 on 2025-02-06 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='intersting',
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
