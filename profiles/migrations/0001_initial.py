# Generated by Django 5.1.3 on 2025-02-13 19:08

import base.utils
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.SlugField(blank=True, default=base.utils.generate_unique_id, editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('gender', models.CharField(blank=True, max_length=12, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('description_myself', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.SlugField(blank=True, default=base.utils.generate_unique_id, editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('address', models.URLField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'SocialMedia',
                'verbose_name_plural': 'SocialMedia',
            },
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.SlugField(blank=True, default=base.utils.generate_unique_id, editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('year', models.PositiveIntegerField()),
                ('moon', models.PositiveIntegerField()),
                ('level', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'verbose_name': 'UserSkill',
                'verbose_name_plural': 'UserSkills',
            },
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.SlugField(blank=True, default=base.utils.generate_unique_id, editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('job_title', models.CharField(blank=True, max_length=200)),
                ('company_name', models.CharField(blank=True, max_length=200)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('is_working', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'WorkHistory',
                'verbose_name_plural': 'WorkHistory',
            },
        ),
    ]
