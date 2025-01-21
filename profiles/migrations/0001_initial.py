# Generated by Django 5.1.3 on 2025-01-21 17:51

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.basemodel')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skill',
                'db_table': '"profile"."skill"',
            },
            bases=('user.basemodel',),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.basemodel')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('description_myself', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
                'db_table': '"profile"."profile"',
            },
            bases=('user.basemodel',),
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.basemodel')),
                ('telegram', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('github', models.URLField(blank=True, null=True)),
                ('gitlab', models.URLField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socialMedia', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'SocialMedia',
                'verbose_name_plural': 'SocialMedia',
                'db_table': '"profile"."social_media"',
            },
            bases=('user.basemodel',),
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.basemodel')),
                ('level', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('skill_reference', models.ManyToManyField(related_name='related_skill', to='profiles.skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_skills', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserSkill',
                'verbose_name_plural': 'UserSkills',
                'db_table': '"profile"."user_skill"',
            },
            bases=('user.basemodel',),
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.basemodel')),
                ('job_title', models.CharField(blank=True, max_length=200)),
                ('company_name', models.CharField(blank=True, max_length=200)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('job_description', models.TextField(blank=True, null=True)),
                ('is_working', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='work_history_entries', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'WorkHistory',
                'verbose_name_plural': 'WorkHistory',
                'db_table': '"profile"."work_history"',
            },
            bases=('user.basemodel',),
        ),
    ]
