from django.contrib import admin

from .models import ErrorLog, RestLog


@admin.register(ErrorLog)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "user", "error_message")
    search_fields = ("error_message",)


@admin.register(RestLog)
class RestLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "user", "action")
    search_fields = ("action",)
