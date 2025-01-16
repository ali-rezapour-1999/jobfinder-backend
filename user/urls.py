from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import UserPersonalViewSet, UserAuthViewSet

router = DefaultRouter()
router.register(r'user-personal', UserPersonalViewSet, basename='user-personal')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserAuthViewSet.as_view({'post': 'register'}), name='user-register'),
    path('login/', UserAuthViewSet.as_view({'post': 'login'}), name='user-login'),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
