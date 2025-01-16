from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .views import (
    UserRegistrationView,
    UserLoginView,
    GoogleLoginView,
    UserProfileViewSet,
)

router = DefaultRouter()
router.register(r'get', UserProfileViewSet, basename='user-profile')

urlpatterns = [
    path('', include(router.urls)),

    path('register/', UserRegistrationView.as_view(), name='user-register'),

    path('login/', UserLoginView.as_view(), name='user-login'),

    path('google-login/', GoogleLoginView.as_view(), name='google-login'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token-verify'),
]
