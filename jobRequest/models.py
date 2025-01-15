from django.db import models

from job.models import Job
from user.models import BaseModel, CustomUser


class JobRequest(BaseModel):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="job_request_user"
    )
    request_job = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name="job_request_job"
    )
    description = models.TextField()
    is_accepted = models.BooleanField(default=False)
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.request_job}"

    class Meta:
        db_table = '"job_request"."job_request"'
        verbose_name = "Job Request"
        verbose_name_plural = "Job Requests"
