from django.contrib import admin
from .models import JobReview, UserReview


@admin.register(UserReview)
class UserReviewAdmin(admin.ModelAdmin):
    list_display = (
        "reviewed_user",
        'reviewer',
        "is_liked",
    )
    search_fields = ("user__username", "reviewed_user__username")
    readonly_fields = ("is_liked",)


@admin.register(JobReview)
class JobReviewAdmin(admin.ModelAdmin):
    list_display = (
        "job_review",
        "user",
        "is_liked",
    )
    search_fields = ("user__username", "job__title")
    readonly_fields = ("is_liked",)
