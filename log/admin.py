from django.contrib import admin

from .models import ErrorLog, RestLog, UserDeviceInfo


@admin.register(ErrorLog)
class ErrorsLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "error_message")
    search_fields = ("error_message",)
    readonly_fields = ("created_at", "updated_at", "slug_id")


@admin.register(RestLog)
class RestLogAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "user", "action")
    search_fields = ("action",)
    readonly_fields = ("created_at", "updated_at", "slug_id")


@admin.register(UserDeviceInfo)
class ErrorLogAdmin(admin.ModelAdmin):
    list_display = ("os", "user_agent", "device_type")
    search_fields = ("ip_address", "timezone", "user_agent", "os")
    readonly_fields = ("created_at", "updated_at", "slug_id")
