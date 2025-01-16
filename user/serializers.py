from django.contrib.auth import get_user_model
from rest_framework import serializers

from user.models import CustomUser

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"], password=validated_data["password"]
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class UserProfileSerializer(serializers.Serializer):
    class Meta:
        model =CustomUser 
        fields = ['email', "phone_number" , 'profile_image' , 'slug' ]


class GoogleLoginSerializer(serializers.Serializer):
    id_token = serializers.CharField()
