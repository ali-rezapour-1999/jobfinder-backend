# Generated by Django 5.1.3 on 2025-02-21 14:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0002_initial'),
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='socialmedia',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialMedia', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userskill',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userskill',
            name='skill_reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_skill', to='base.tags'),
        ),
        migrations.AddField(
            model_name='userskill',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userskill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_skills', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workhistory',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_create_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workhistory',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='%(class)s_updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='workhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_history', to=settings.AUTH_USER_MODEL),
        ),
    ]
