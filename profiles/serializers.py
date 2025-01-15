from rest_framework import serializers

from .models import Profile, Review, Skill, WorkHistory


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["id", "name"]


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
    skills = SkillSerializer(many=True, read_only=True)
    work_history_entries = WorkHistorySerializer(many=True, read_only=True)
    email = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = "__all__"

    def get_email(self, obj):
        return obj.user.email if obj.user else None


class ReviewSerializer(serializers.ModelSerializer):
    total_likes = serializers.IntegerField(source='total_likes', read_only=True)
    total_dislikes = serializers.IntegerField(source='total_dislikes', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'likes', 'dislikes', 'total_likes', 'total_dislikes']
        read_only_fields = ['total_likes', 'total_dislikes']
