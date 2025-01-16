from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from core.utils import generate_unique_id, validate_iranian_phone_number
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    slug_id = models.CharField(max_length=8, unique=True, default=generate_unique_id)
    email = models.EmailField(
        unique=True,
    )
    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )
    phone_number = models.CharField(
        max_length=11,
        unique=True,
        blank=True,
        null=True,
        validators=[validate_iranian_phone_number],
    )
    username = models.CharField(max_length=100, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        db_table = '"auth"."custom_user"'
        verbose_name = "User"
        verbose_name_plural = "User"

    def __str__(self):
        return self.email


class BaseModel(models.Model):
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

    class Mete:
        abstract = True
