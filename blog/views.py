from rest_framework import permissions, viewsets
from log.models import ErrorLog, RestLog
from .models import Category, Post
from .serializers import PostSerializers, CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(is_active=True)
    serializer_class = PostSerializers
    lookup_field = "slug_id"
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            post = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="post Created",
                request_data=self.request.data,
                response_data=PostSerializers(post).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="post creation failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e

    def perform_update(self, serializer):
        try:
            post = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Post Updated",
                request_data=self.request.data,
                response_data=PostSerializers(post).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Post update failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e

    def perform_destroy(self, instance):
        try:
            instance.delete()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Post Deleted",
                request_data=self.request.data,
                response_data={"slug_id": instance.slug_id},
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Post failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e


class CatagoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer
    lookup_field = "slug_id"
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        try:
            category = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Tag Created",
                request_data=self.request.data,
                response_data=CategorySerializer(category).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Category creation failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e

    def perform_update(self, serializer):
        try:
            category = serializer.save()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Catagory Updated",
                request_data=self.request.data,
                response_data=CategorySerializer(category).data,
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Category update failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e

    def perform_destroy(self, instance):
        try:
            instance.delete()
            RestLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action="Category Deleted",
                request_data=self.request.data,
                response_data={"slug_id": instance.slug_id},
            )
        except Exception as e:
            ErrorLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                error_message="Category failed",
                stack_trace=str(e),
                request_data=self.request.data,
            )
            raise e
