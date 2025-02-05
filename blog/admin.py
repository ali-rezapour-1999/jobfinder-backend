from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("user", "slug_id", "is_active", "created_at")
    list_filter = ("status", "categories", "tags", "user", "is_active")
    search_fields = (
        "user__email",
        "user__phone_number",
    )
    readonly_fields = ("created_at", "updated_at", "slug_id", "views")
    fieldsets = (
        (
            "Personal Info",
            {
                "fields": (
                    "slug_id",
                    "user",
                    "categories",
                    "tags",
                    "views",
                    "image",
                )
            },
        ),
        (
            "Post",
            {
                "fields": (
                    "title",
                    "content",
                    "publish",
                )
            },
        ),
        ("Other Info", {"fields": ("is_active", "created_at", "updated_at")}),
    )


@admin.register(Category)
class CatagoryMediaAdmin(admin.ModelAdmin):
    list_display = ("slug_id", "is_active", "created_at")
    list_filter = ("title", "is_active")
    readonly_fields = ("created_at", "updated_at", "slug_id")
    fieldsets = (
        (
            "Personal Info",
            {"fields": ("slug_id", "title")},
        ),
        ("Other Info", {"fields": ("is_active", "created_at", "updated_at")}),
    )
