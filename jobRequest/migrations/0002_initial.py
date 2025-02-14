# Generated by Django 5.1.3 on 2025-02-14 15:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('job', '0002_initial'),
        ('jobRequest', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='jobrequest',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='request_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_request_job', to='job.job'),
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='jobrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_request_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
