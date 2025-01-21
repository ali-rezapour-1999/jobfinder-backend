from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import JobReviewViewSet, UserReviewViewSet

router = DefaultRouter()
router.register(r"job_reviews", JobReviewViewSet, basename="job_review")
router.register(r"user_reviews", UserReviewViewSet, basename="user_review")

urlpatterns = [
    path("", include(router.urls)),
]
