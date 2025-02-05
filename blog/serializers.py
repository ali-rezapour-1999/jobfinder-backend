from rest_framework import serializers
from .models import Post, Category
from base.serializers import TagsSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = "__all__"


class PostSerializers(serializers.ModelSerializer):
    tags = TagsSerializer(read_only=True)
    categories = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        field = "__all__"
