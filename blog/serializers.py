from rest_framework import serializers
from .models import Post
from base.serializers import TagsSerializer


class PostSerializers(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True)

    class Meta:
        model = Post
        field = "__all__"
