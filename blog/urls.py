from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CatagoryViewSet, PostViewSet

router = DefaultRouter()
router.register("post", PostViewSet)
router.register("catagory", CatagoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
