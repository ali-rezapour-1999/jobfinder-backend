from django.contrib import admin

from .models import Profile, Skill, SocialMedia, UserSkill, WorkHistory


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    def get_fieldsets(self, obj=None):
        fields = [
            field.name for field in obj._meta.get_fieldsets() if not field.auto_created
        ]
        fields = [f for f in fields if f not in ("created_at", "updated_at")]
        return [
            ("Main Information", {"fields": fields}),
            ("Timestamps", {"fields": ("created_at", "updated_at")}),
        ]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "is_active", "created_at")
    list_filter = ("gender", "state", "city", "is_active")
    search_fields = ("user__email", "user__phone_number")
    readonly_fields = ("created_at", "updated_at")
    fieldsets = (
        (
            "Personal Info",
            {
                "fields": (
                    "user",
                    "age",
                    "gender",
                    "my_skill",
                )
            },
        ),
        ("Address", {"fields": ("state", "city", "address")}),
        ("Professional Info", {"fields": ("description_myself",)}),
        ("Other Info", {"fields": ("is_active", "created_at", "updated_at")}),
    )


@admin.register(WorkHistory)
class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "job_title", "company_name",
                    "start_date", "end_date")
    list_filter = ("company_name", "start_date", "end_date")
    search_fields = ("job_title", "company_name")
    date_hierarchy = "start_date"
    fields = (
        "user",
        "job_title",
        "company_name",
        "start_date",
        "end_date",
        "job_description",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(UserSkill)
class UserSkillAdmin(admin.ModelAdmin):
    list_display = (
        "skill",
        "user",
    )
    search_fields = (
        "user",
        "skill",
    )
