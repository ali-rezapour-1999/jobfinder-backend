from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, UserSkillViewSet, WorkHistoryViewSet

router = DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("work-history", WorkHistoryViewSet)
router.register("skills", UserSkillViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
