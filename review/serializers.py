from rest_framework import serializers

from .models import JobReview, UserReview


class JobReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobReview
        fields = ["job", "user", "is_liked"]


class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ["reviewed_user", "reviewer", "is_liked"]
