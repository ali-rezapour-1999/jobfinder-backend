# Generated by Django 5.1.3 on 2025-02-14 15:05

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.SlugField(blank=True, default=base.utils.generate_unique_id, editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Tags',
                'verbose_name_plural': 'Tags',
            },
        ),
    ]
