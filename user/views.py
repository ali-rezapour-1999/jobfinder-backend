from django.conf import settings
from django.contrib.auth import authenticate, get_user_model
from google.auth.transport import requests
from google.oauth2 import id_token
from rest_framework import status , viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from log.models import ErrorLog, RestLog
from user.models import CustomUser

from .serializers import (GoogleLoginSerializer, UserLoginSerializer, UserProfileSerializer,
                          UserRegistrationSerializer)

User = get_user_model()

class UserPersonalViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "slug_id"
    permission_classes = [IsAuthenticated]

class UserAuthViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
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
                    "user": {"email": user.email},
                },
            )

            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user": {"email": user.email},
                },
                status=status.HTTP_201_CREATED,
            )

        ErrorLog.objects.create(
            user=None,
            error_message="User registration failed",
            request_data=request.data,
        )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
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

    @action(detail=False, methods=['post'])
    def google_login(self, request):
        serializer = GoogleLoginSerializer(data=request.data)
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

                # Log successful Google login
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
