from django.db import transaction
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from log.models import ErrorLog, RestLog
from .models import Profile, Review, Skill, WorkHistory
from .serializers import ProfileSerializer, ReviewSerializer, SkillSerializer, WorkHistorySerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "user__slug_id"
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
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Profile creation failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
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
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Profile update failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
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
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Profile deletion failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e


class WorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

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
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Work history creation failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
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
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Work history update failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
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
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Work history deletion failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            skill = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Skill Created",
                request_data=self.request.data,
                response_data=SkillSerializer(skill).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Skill creation failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e

    def perform_update(self, serializer):
        try:
            skill = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Skill Updated",
                request_data=self.request.data,
                response_data=SkillSerializer(skill).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Skill update failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e

    def perform_destroy(self, instance):
        try:
            instance.delete()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Skill Deleted",
                request_data=self.request.data,
                response_data={"id": instance.id},
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Skill deletion failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def _toggle_reaction(self, review, user, reaction_field, opposite_field):
        with transaction.atomic():
            if user in getattr(review, opposite_field).all():
                getattr(review, opposite_field).remove(user)
            if user not in getattr(review, reaction_field).all():
                getattr(review, reaction_field).add(user)
            else:
                getattr(review, reaction_field).remove(user)

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        review = self.get_object()  # Automatically handles DoesNotExist
        self._toggle_reaction(review, request.user, "likes", "dislikes")
        serializer = self.get_serializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def dislike(self, request, pk=None):
        review = self.get_object()
        self._toggle_reaction(review, request.user, "dislikes", "likes")
        serializer = self.get_serializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
