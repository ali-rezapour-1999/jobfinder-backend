from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, WorkHistoryViewSet, SkillViewSet,ReviewViewSet 

router = DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("work-history", WorkHistoryViewSet)
router.register("skills", SkillViewSet)
router.register(r'reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path("", include(router.urls)),
]
