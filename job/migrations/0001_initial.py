# Generated by Django 5.1.3 on 2024-12-29 19:13

import core.utils
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="user.basemodel",
                    ),
                ),
                (
                    "slug_id",
                    models.CharField(
                        default=core.utils.generate_unique_id, max_length=8, unique=True
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255)),
                ("main_title", models.CharField(blank=True, max_length=255)),
                (
                    "job_image",
                    models.ImageField(blank=True, null=True, upload_to="job_images/"),
                ),
                ("desciption", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            bases=("user.basemodel",),
        ),
        migrations.CreateModel(
            name="JobOptions",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="user.basemodel",
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "job",
                    models.ManyToManyField(related_name="job_options", to="job.job"),
                ),
            ],
            bases=("user.basemodel",),
        ),
        migrations.CreateModel(
            name="SkillNeeded",
            fields=[
                (
                    "basemodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="user.basemodel",
                    ),
                ),
                (
                    "slug_id",
                    models.CharField(
                        default=core.utils.generate_unique_id, max_length=8, unique=True
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "level",
                    models.DecimalField(
                        decimal_places=1,
                        max_digits=5,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                ("description", models.TextField()),
                (
                    "job",
                    models.ManyToManyField(
                        related_name="job_skillneeded", to="job.job"
                    ),
                ),
            ],
            bases=("user.basemodel",),
        ),
    ]
