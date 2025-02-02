# Generated by Django 5.1.3 on 2025-02-02 18:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',), 'verbose_name': 'post', 'verbose_name_plural': 'post'},
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
