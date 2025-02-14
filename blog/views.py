from rest_framework import permissions, viewsets
from log.models import ErrorLog, RestLog
from .models import Category, Post
from .serializers import PostSerializers, CategorySerializer


class BasePostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializers
    lookup_field = "slug_id"
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Subclasses should override this method to filter posts."""
        return Post.objects.none()

    def log_action(self, action, post):
        """Helper method to log successful actions."""
        RestLog.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            action=action,
            request_data=self.request.data,
            response_data=PostSerializers(post).data
            if post
            else {"slug_id": self.kwargs.get("slug_id")},
        )

    def log_error(self, error_message, exception):
        """Helper method to log errors."""
        ErrorLog.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            error_message=error_message,
            stack_trace=str(exception),
            request_data=self.request.data,
        )

    def perform_create(self, serializer):
        try:
            post = serializer.save()
            self.log_action("Post Created", post)
        except Exception as e:
            self.log_error("Post creation failed", e)
            raise e

    def perform_update(self, serializer):
        try:
            post = serializer.save()
            self.log_action("Post Updated", post)
        except Exception as e:
            self.log_error("Post update failed", e)
            raise e

    def perform_destroy(self, instance):
        try:
            slug_id = instance.slug_id
            instance.delete()
            self.log_action("Post Deleted", None)
        except Exception as e:
            self.log_error("Post deletion failed", e)
            raise e


class PostViewSet(BasePostViewSet):
    """Handles published posts."""

    def get_queryset(self):
        return Post.objects.filter(status="published", is_active=True)


class PostDraftViewSet(BasePostViewSet):
    """Handles draft posts."""

    def get_queryset(self):
        return Post.objects.filter(status="draft", is_active=True)


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
