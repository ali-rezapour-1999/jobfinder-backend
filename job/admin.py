from django.contrib import admin

from job.models import Job, SkillNeeded

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('slug_id_registertin', 'title', 'user')
    search_fields = ('title', 'slug_id')
    list_filter = ('user',)

#this for test in my file
@admin.register(SkillNeeded)
class SkillNeededAdmin(admin.ModelAdmin):
    list_display = ('slug_name', 'title', 'level')
    search_fields = ('title', 'slug_id')
    list_filter = ('level',)
