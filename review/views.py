from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from log.models import ErrorLog, RestLog
from .models import JobReview, UserReview
from .serializers import JobReviewSerializer, UserReviewSerializer


class JobReviewViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = JobReview.objects.all()
    serializer_class = JobReviewSerializer

    def perform_create(self, serializer):
        try:
            job_review = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="job review Created",
                request_data=self.request.data,
                response_data=JobReviewSerializer(job_review).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="job review creation failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e

    def perform_update(self, serializer):
        try:
            job_review = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Job Review Updated",
                request_data=self.request.data,
                response_data=JobReviewSerializer(job_review).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="job review update failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e


class UserReviewViewSet(CreateModelMixin, viewsets.GenericViewSet):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer

    def perform_create(self, serializer):
        try:
            user_review = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="user review Created",
                request_data=self.request.data,
                response_data=UserReviewSerializer(user_review).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="user review creation failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e

    def perform_update(self, serializer):
        try:
            user_review = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="user Review Updated",
                request_data=self.request.data,
                response_data=UserReviewSerializer(user_review).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="user review update failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e
