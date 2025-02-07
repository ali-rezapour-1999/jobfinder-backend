from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CatagoryViewSet, PostViewSet, PostDraftViewSet

router = DefaultRouter()
router.register("post", PostViewSet, basename="post")
router.register("post-draft", PostDraftViewSet, basename="draft-post")
router.register("catagory", CatagoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
