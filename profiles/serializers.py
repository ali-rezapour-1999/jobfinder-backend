from rest_framework import serializers
from .models import Profile, WorkHistory, SocialMedia, UserSkill
from base.serializers import TagsSerializer


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = ["id", "title", "address"]


class UserSkillSerializer(serializers.ModelSerializer):
    skill_reference = TagsSerializer(read_only=True)

    class Meta:
        model = UserSkill
        fields = "__all__"


class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Profile

    def get_email(self, obj):
        return obj.user.email if obj.user else None
