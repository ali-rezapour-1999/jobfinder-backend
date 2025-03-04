# Generated by Django 5.1.3 on 2025-02-21 14:49

import base.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.SlugField(blank=True, default=base.utils.generate_unique_id, editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('request_path', models.CharField(max_length=512)),
                ('request_method', models.CharField(max_length=10)),
                ('request_body', models.TextField(blank=True, null=True)),
                ('response_status', models.IntegerField()),
                ('response_message', models.TextField()),
                ('traceback_info', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RestLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.SlugField(blank=True, default=base.utils.generate_unique_id, editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(max_length=255)),
                ('request_data', models.JSONField(blank=True, null=True)),
                ('response_data', models.JSONField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'rest_log',
                'verbose_name_plural': 'rest_log',
            },
        ),
        migrations.CreateModel(
            name='UserDeviceInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.SlugField(blank=True, default=base.utils.generate_unique_id, editable=False, max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('ip_address', models.TextField(blank=True, null=True)),
                ('user_agent', models.TextField()),
                ('device_type', models.CharField(blank=True, max_length=100, null=True)),
                ('browser', models.CharField(blank=True, max_length=100, null=True)),
                ('os', models.CharField(blank=True, max_length=100, null=True)),
                ('screen_resolution', models.TextField(blank=True, null=True)),
                ('timezone', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'UserDeviceInfo',
                'verbose_name_plural': 'UserDeviceInfo',
            },
        ),
    ]
