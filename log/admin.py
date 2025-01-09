from django.contrib import admin

from .models import ErrorLog, RestLog


@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "message")
    search_fields = ("message",)


@admin.register(RestLog)
class RestLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "user", "status_code")
    search_fields = ("status_code",)
