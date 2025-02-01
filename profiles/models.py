from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from user.middleware import get_current_user
from user.models import BaseModel, CustomUser


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


class Profile(BaseModel):
    gender_choices = [
        ("M", "Male"),
        ("F", "Female"),
    ]
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="profile"
    )
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=gender_choices, blank=True, null=True
    )
    state = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    description_myself = models.TextField(blank=True, null=True)
    my_skill = models.ManyToManyField(Skill, related_name="my_skill")

    def __str__(self):
        return f"{self.user.first_last_name}"

    class Meta:
        db_table = '"profile"."profile"'
        verbose_name = "Profile"
        verbose_name_plural = "Profile"


class WorkHistory(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="work_history"
    )
    job_title = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(null=True, blank=True)
    job_description = models.TextField(blank=True, null=True)
    is_working = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"

    class Meta:
        db_table = '"profile"."work_history"'
        verbose_name = "WorkHistory"
        verbose_name_plural = "WorkHistory"


class UserSkill(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="user_skills"
    )
    skill_reference = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name="related_skill"
    )
    year = models.PositiveIntegerField()
    moon = models.PositiveIntegerField()
    level = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=True,
        blank=True,
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
    address = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        db_table = '"profile"."social_media"'
        verbose_name = "SocialMedia"
        verbose_name_plural = "SocialMedia"

    def __str__(self):
        return f"{self.user} - {self.address}"
