from rest_framework import permissions, viewsets
from log.models import RestLog
from .models import Profile, WorkHistory, SocialMedia, UserSkill
from rest_framework.response import Response
from .serializers import (
    ProfileSerializer,
    WorkHistorySerializer,
    SocialMediaSerializer,
    UserSkillSerializer,
)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.select_related("user").filter(is_active=True)
    lookup_field = "user__slug_id"
    serializer_class = ProfileSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        try:
            profile = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Profile Created",
                request_data=self.request.data,
                response_data=ProfileSerializer(profile).data,
            )
        except Exception as e:
            raise e

    def perform_update(self, serializer):
        try:
            profile = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Profile Updated",
                request_data=self.request.data,
                response_data=ProfileSerializer(profile).data,
            )
        except Exception as e:
            raise e

    def perform_destroy(self, instance):
        try:
            instance.delete()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Profile Deleted",
                request_data=self.request.data,
                response_data={"slug_id": instance.slug_id},
            )
        except Exception as e:
            raise e


class WorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WorkHistory.objects.select_related("user").filter(is_active=True)
    serializer_class = WorkHistorySerializer
    lookup_field = "user__slug_id"
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        try:
            work_history = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Work History Created",
                request_data=self.request.data,
                response_data=WorkHistorySerializer(work_history).data,
            )
        except Exception as e:
            raise e

    def perform_update(self, serializer):
        try:
            work_history = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Work History Updated",
                request_data=self.request.data,
                response_data=WorkHistorySerializer(work_history).data,
            )
        except Exception as e:
            raise e

    def perform_destroy(self, instance):
        try:
            instance.delete()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Work History Deleted",
                request_data=self.request.data,
                response_data={"id": instance.id},
            )
        except Exception as e:
            raise e


class SocialMediaViewSet(viewsets.ModelViewSet):
    serializer_class = SocialMediaSerializer
    lookup_field = "slug_id"
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return SocialMedia.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        social_media = serializer.save(user=self.request.user)
        RestLog.objects.create(
            user=self.request.user,
            action="SocialMedia Created",
            request_data=self.request.data,
            response_data=SocialMediaSerializer(social_media).data,
        )

    def perform_update(self, serializer):
        social_media = serializer.save()
        RestLog.objects.create(
            user=self.request.user,
            action="SocialMedia Updated",
            request_data=self.request.data,
            response_data=SocialMediaSerializer(social_media).data,
        )

    def perform_destroy(self, instance):
        instance.delete()
        RestLog.objects.create(
            user=self.request.user,
            action="SocialMedia Deleted",
            request_data=self.request.data,
            response_data={"id": instance.id},
        )


class UserSkillViewSet(viewsets.ModelViewSet):
    queryset = UserSkill.objects.select_related("user").filter(is_active=True)
    serializer_class = UserSkill
    lookup_field = "user__slug_id"
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            user_skill = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="User Skill Created",
                request_data=self.request.data,
                response_data=UserSkillSerializer(user_skill).data,
            )
        except Exception as e:
            raise e

    def perform_update(self, serializer):
        try:
            user_skill = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="User Skill Updated",
                request_data=self.request.data,
                response_data=UserSkillSerializer(user_skill).data,
            )
        except Exception as e:
            raise e

    def perform_destroy(self, instance):
        try:
            instance.delete()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="User Skill Deleted",
                request_data=self.request.data,
                response_data={"id": instance.id},
            )
        except Exception as e:
            raise e
