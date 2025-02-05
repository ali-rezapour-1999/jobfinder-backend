from django.contrib import admin
from .models import Tags


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    readonly_fields = ("created_at", "updated_at", "slug_id")
    ordering = ("title",)
