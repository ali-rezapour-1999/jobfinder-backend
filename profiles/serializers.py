from rest_framework import serializers

from .models import Profile, Skill, WorkHistory, SocialMedia


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name"]


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ["id", "title", "address"]


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = [
            "id",
            "job_title",
            "company_name",
            "start_date",
            "end_date",
            "job_description",
        ]


class ProfileSerializer(serializers.ModelSerializer):
    my_skill = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = "__all__"

    def get_email(self, obj):
        return obj.user.email if obj.user else None
