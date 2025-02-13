from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from user.models import CustomUser
from base.models import BaseModel, Tags


class Job(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="jobs")
    title = models.CharField(max_length=255, null=False, blank=True)
    main_title = models.CharField(max_length=255, null=False, blank=True)
    job_image = models.ImageField(
        upload_to="job_images/", null=True, blank=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tags, related_name="jobs")
    is_approve = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.user}"

    class Meta:
        verbose_name = "Job"
        verbose_name_plural = "Jobs"


class SkillNeeded(BaseModel):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="skills")
    title = models.CharField(max_length=255, null=True, blank=True)
    level = models.DecimalField(
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.job.title}"

    class Meta:
        verbose_name = "Skill Needed"
        verbose_name_plural = "Skills Needed"


class JobOption(BaseModel):
    job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="options")
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.job.title}"

    class Meta:
        verbose_name = "Job Option"
        verbose_name_plural = "Job Options"
