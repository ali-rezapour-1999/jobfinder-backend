from rest_framework import serializers
from .models import Post, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        field = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = "__all__"


class PostSerializers(serializers.ModelSerializer):
    tags = TagSerializer(read_only=True)
    categories = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        field = "__all__"
