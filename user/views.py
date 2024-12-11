from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from google.oauth2 import id_token
from google.auth.transport import requests

from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    GoogleLoginSerializer
)
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {'email': user.email}
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, email=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {'email': user.email}
                })

            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GoogleLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = GoogleLoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                id_info = id_token.verify_oauth2_token(
                    serializer.validated_data['id_token'],
                    requests.Request(),
                    settings.GOOGLE_CLIENT_ID
                )

                user, created = User.objects.get_or_create(
                    google_id=id_info['sub'],
                    defaults={
                        'email': id_info['email'],
                        'is_active': True
                    }
                )

                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {'email': user.email, 'is_new': created}
                })

            except ValueError:
                return Response(
                    {'error': 'Invalid Google token'},
                    status=status.HTTP_401_UNAUTHORIZED
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
