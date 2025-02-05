from django.db import models
from user.middleware import get_current_user
from base.utils import generate_unique_id
from user.models import CustomUser


class BaseModel(models.Model):
    slug_id = models.SlugField(
        max_length=8,
        unique=True,
        blank=True,
        default=generate_unique_id,
        editable=False,
    )
    create_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_create_by",
    )
    updated_by = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated_by",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Tags(BaseModel):
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = '"base"."tags"'
        verbose_name = "Tags"
        verbose_name_plural = "Tags"

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.create_by = user
        self.updated_by = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
