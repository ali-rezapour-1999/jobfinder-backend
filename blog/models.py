from django.db import models
from user.models import BaseModel, CustomUser
from django.utils import timezone
from taggit.managers import TaggableManager


class Tag(BaseModel):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '"blog"."tag"'
        verbose_name = "Tag"
        verbose_name_plural = "Tag"


class Category(BaseModel):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = '"blog"."category"'
        verbose_name = "category"
        verbose_name_plural = "category"


class Post(BaseModel):
    title = models.CharField(max_length=500, null=False, blank=False)
    user = models.ForeignKey(
        CustomUser, related_name="post_user", on_delete=models.CASCADE
    )
    content = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=[("draft", "Draft"), ("published", "Published")],
        default="draft",
    )
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True)
    categories = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="posts", blank=True
    )
    image = models.ImageField(upload_to="blog/%Y/%m/%d/", blank=True)
    views = models.PositiveIntegerField(default=0)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-publish",)
        db_table = '"blog"."post"'
        verbose_name = "post"
        verbose_name_plural = "post"
