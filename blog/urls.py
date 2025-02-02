from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CatagoryViewSet, TagViewSet, PostViewSet

router = DefaultRouter()
router.register("post", PostViewSet)
router.register("tag", TagViewSet)
router.register("catagory", CatagoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
