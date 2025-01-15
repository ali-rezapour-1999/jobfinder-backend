from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Create schemas if they do not exist'

    def handle(self, *args, **kwargs):
        schemas = ['public', 'auth', 'profile', 'log', 'job', 'job_request']
        with connection.cursor() as cursor:
            for schema in schemas:
                cursor.execute(f"""
                    DO $$ BEGIN
                        IF NOT EXISTS (SELECT 1 FROM pg_catalog.pg_namespace WHERE nspname = '{schema}') THEN
                            EXECUTE 'CREATE SCHEMA {schema}';
                        END IF;
                    END $$;
                """)
                self.stdout.write(self.style.SUCCESS(f'Schema "{schema}" checked/created successfully.'))

