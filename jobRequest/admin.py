from django.contrib import admin

from .models import JobRequest


@admin.register(JobRequest)
class JobRequestAdmin(admin.ModelAdmin):
    list_display = ("user", "request_job")
    search_fields = ("request_job", "user")
