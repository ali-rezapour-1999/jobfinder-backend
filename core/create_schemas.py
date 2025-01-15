from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Creates schemas for all apps'

    def handle(self, *args, **kwargs):
        apps = ['auth', 'profile', 'log', 'job', 'job_request']
        with connection.cursor() as cursor:
            for app in apps:
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {app};")
        self.stdout.write(self.style.SUCCESS('Schemas created successfully'))
