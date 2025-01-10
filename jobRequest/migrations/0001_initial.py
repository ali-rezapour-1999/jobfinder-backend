# Generated by Django 5.1.3 on 2025-01-10 09:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("job", "0001_initial"),
        ("user", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="JobRequest",
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
                ("description", models.TextField()),
                ("is_accepted", models.BooleanField(default=False)),
                ("is_cancelled", models.BooleanField(default=False)),
                (
                    "request_job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_request_job",
                        to="job.job",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="job_request_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Job Request",
                "verbose_name_plural": "Job Requests",
            },
            bases=("user.basemodel",),
        ),
    ]
