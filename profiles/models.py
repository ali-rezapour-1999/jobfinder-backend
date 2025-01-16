from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from core.utils import generate_unique_id
from user.middleware import get_current_user
from user.models import BaseModel, CustomUser

class Profile(BaseModel):
    gender_choices = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    slug_id = models.CharField(max_length=8, unique=True, default=generate_unique_id , blank=True , null=True)
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    first_name = models.CharField(max_length=100, blank=True , null=True)
    last_name = models.CharField(max_length=100, blank=True , null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True  , null=True)
    state = models.CharField(max_length=100, blank=True , null=True)
    city = models.CharField(max_length=100, blank=True , null =True)
    address = models.TextField(blank=True, null=True)

    description_myself = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.username}"

    class Meta:
        db_table = '"profile"."profile"'
        verbose_name = "Profile"
        verbose_name_plural = "Profile"


class WorkHistory(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="work_history_entries"
    )
    job_title = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(blank=True , null=True)
    end_date = models.DateField(null=True, blank=True)
    job_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    class Meta:
        db_table = '"profile"."work_history"'
        verbose_name = "WorkHistory"
        verbose_name_plural = "WorkHistory"


class Skill(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = '"profile"."skill"'
        verbose_name = "Skill"
        verbose_name_plural = "Skill"

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.create_by = user
        self.updated_by = user
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class UserSkill(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_skills"
    )
    skill_reference = models.ManyToManyField(Skill, related_name="related_skill")
    level = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=True, blank=True
    )

    def __str__(self):
        return f"{self.user} - {self.skill_reference}"

    class Meta:
        db_table = '"profile"."user_skill"'
        verbose_name = "UserSkill"
        verbose_name_plural = "UserSkills"


class SocialMedia(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="socialMedia"
    )
    telegram = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    gitlab = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    class Meta:
        db_table = '"profile"."social_media"'
        verbose_name = "SocialMedia"
        verbose_name_plural = "SocialMedia"

    def __str__(self):
        return f"{self.user}"


class Review(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="reviews"
    )
    likes = models.ManyToManyField(CustomUser, related_name="liked_reviews", blank=True)
    dislikes = models.ManyToManyField(CustomUser, related_name="disliked_reviews", blank=True)

    class Meta:
        db_table = '"profile"."review"'
        verbose_name = "Review"
        verbose_name_plural = "Review"
