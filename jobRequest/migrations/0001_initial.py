# Generated by Django 5.1.3 on 2025-02-14 15:05

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.SlugField(blank=True, default=base.utils.generate_unique_id, editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Job Request',
                'verbose_name_plural': 'Job Requests',
            },
        ),
    ]
