from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from log.models import ErrorLog, RestLog
from user.models import CustomUser

from .serializers import (
    GoogleLoginSerializer,
    UserDetailSerializer,
    UserLoginSerializer,
    UserRegistrationSerializer,
)

User = get_user_model()


class UserRegistrationView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            RestLog.objects.create(
                user=user,
                action="User Registration",
                request_data=request.data,
                response_data={
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": {"email": user.email, "slug": user.slug_id},
                },
            )
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": {"email": user.email, "slug": user.slug_id},
                },
                status=status.HTTP_201_CREATED,
            )
        ErrorLog.objects.create(
            user=None,
            error_message="User registration failed",
            request_data=request.data,
        )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = User.objects.filter(email=email).first()

            if not user:
                ErrorLog.objects.create(
                    user=None,
                    error_message="User not found",
                    request_data=request.data,
                )
                return Response(
                    {"error": "NOT_FOUND"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            user = authenticate(request, email=email, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                RestLog.objects.create(
                    user=user,
                    action="User Login",
                    request_data=request.data,
                    response_data={
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user": {"email": user.email, "slug": user.slug_id},
                    },
                )
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user": {"email": user.email, "slug": user.slug_id},
                    }
                )
            ErrorLog.objects.create(
                user=user,
                error_message="Incorrect password",
                request_data=request.data,
            )
            return Response(
                {"error": "PASSWORD_INVALID"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        ErrorLog.objects.create(
            user=None,
            error_message="Invalid login request data",
            request_data=serializer.errors,
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleLoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = GoogleLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            try:
                id_info = id_token.verify_oauth2_token(
                    serializer.validated_data["id_token"],
                    requests.Request(),
                    settings.GOOGLE_CLIENT_ID,
                )
                user, created = User.objects.get_or_create(
                    google_id=id_info["sub"],
                    defaults={"email": id_info["email"], "is_active": True},
                )
                refresh = RefreshToken.for_user(user)
                RestLog.objects.create(
                    user=user,
                    action="Google Login",
                    request_data=request.data,
                    response_data={
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user": {"email": user.email, "is_new": created},
                    },
                )
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user": {"email": user.email, "is_new": created},
                    }
                )
            except ValueError as e:
                ErrorLog.objects.create(
                    user=None,
                    error_message="Invalid Google token",
                    stack_trace=str(e),
                    request_data=request.data,
                )
                return Response(
                    {"error": "Invalid Google token"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        ErrorLog.objects.create(
            user=None,
            error_message="Invalid Google login request data",
            request_data=serializer.errors,
        )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = "slug_id"
    permission_classes = [AllowAny]

    @action(detail=False, methods=["get"])
    def me(self, request):
        serializer = self.get_serializer(request.user)
        RestLog.objects.create(
            user=request.user,
            action="Get User Data",
            request_data={},
            response_data=serializer.data,
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
