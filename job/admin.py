from django.contrib import admin
from job.models import Job, JobOption, SkillNeeded


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("slug_id", "title", "user")
    search_fields = ("title", "slug_id")
    list_filter = ("user",)


@admin.register(SkillNeeded)
class SkillNeededAdmin(admin.ModelAdmin):
    list_display = ("slug_id", "title", "level")
    search_fields = ("title", "slug_id")
    list_filter = ("level",)


@admin.register((JobOption))
class JobOptionsAdmin(admin.ModelAdmin):
    list_display = ("slug_id", "title")
    search_fields = ("title", "slug_id")
