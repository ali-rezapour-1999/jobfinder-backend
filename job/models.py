from django.contrib.auth.models import models
from django.core.validators import MaxValueValidator, MinValueValidator

from core.utils import generate_unique_id
from user.models import BaseModel, CustomUser

class Job(BaseModel):
    slug_id = models.CharField(max_length=8, unique=True, default=generate_unique_id)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=255, null=False, blank=True)
    main_title = models.CharField(max_length=255, null=False, blank=True)
    job_image = models.ImageField(upload_to="job_images/", null=True, blank=True)
    desciption = models.TextField()

    def __str__(self):
        return f"{self.title} and {self.user}"


class SkillNeeded(BaseModel):
    slug_id = models.CharField(max_length=8, unique=True, default=generate_unique_id)
    job = models.ManyToManyField(Job, related_name="job_skillneeded")
    title = models.CharField(max_length=255, null=True, blank=True)
    level = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.title} and {self.job}"


class JobOptions(BaseModel):
    slug_id = models.CharField(max_length=8, unique=True, default=generate_unique_id)
    job = models.ManyToManyField(Job, related_name="job_options")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} and {self.job}"
