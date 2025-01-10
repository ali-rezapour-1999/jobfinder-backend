from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError

from log.models import ErrorLog, RestLog

from .models import Profile, Skill, WorkHistory
from .serializers import (ProfileSerializer, SkillSerializer,
                          WorkHistorySerializer)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = "slug_id"
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)

            RestLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action="Profile List View",
                request_data=request.query_params.dict(),
                response_data=response.data,
            )
            return response

        except ValidationError as e:

            ErrorLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                error_message="Validation error in Profile list",
                stack_trace=str(e),
                request_data=request.query_params.dict(),
            )
            raise e

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            RestLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action="Profile Create View",
                request_data=request.data,
                response_data=response.data,
            )
            return response

        except ValidationError as e:
            ErrorLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                error_message="Validation error in Profile create",
                stack_trace=str(e),
                request_data=request.data,
            )
            raise e


class WorkHistoryViewSet(viewsets.ModelViewSet):
    queryset = WorkHistory.objects.all()
    serializer_class = WorkHistorySerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)

            RestLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action="Work History List View",
                request_data=request.query_params.dict(),
                response_data=response.data,
            )
            return response

        except ValidationError as e:
            ErrorLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                error_message="Validation error in Work History list",
                stack_trace=str(e),
                request_data=request.query_params.dict(),
            )
            raise e  # Re-raise the error after logging

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)

            RestLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action="Work History Create View",
                request_data=request.data,
                response_data=response.data,
            )
            return response

        except ValidationError as e:
            ErrorLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                error_message="Validation error in Work History create",
                stack_trace=str(e),
                request_data=request.data,
            )
            raise e


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)

            RestLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action="Skill List View",
                request_data=request.query_params.dict(),
                response_data=response.data,
            )
            return response

        except ValidationError as e:
            ErrorLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                error_message="Validation error in Skill list",
                stack_trace=str(e),
                request_data=request.query_params.dict(),
            )
            raise e

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)

            RestLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                action="Skill Create View",
                request_data=request.data,
                response_data=response.data,
            )
            return response

        except ValidationError as e:
            ErrorLog.objects.create(
                user=request.user if request.user.is_authenticated else None,
                error_message="Validation error in Skill create",
                stack_trace=str(e),
                request_data=request.data,
            )
            raise e
