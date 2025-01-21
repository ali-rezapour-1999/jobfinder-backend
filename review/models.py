from django.db import models
from job.models import Job
from user.models import CustomUser, BaseModel


class UserReview(BaseModel):
    reviewed_user = models.ForeignKey(
        CustomUser, related_name="reviews", on_delete=models.CASCADE)
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_liked = models.BooleanField()

    def __str__(self):
        return f"Review for {self.reviewed_user} by {self.reviewer}"

    class Meta:
        db_table = '"review"."user_review"'
        verbose_name = "User_Review"


class JobReview(BaseModel):
    job_review = models.ForeignKey(
        Job, on_delete=models.CASCADE, related_name='job_review')
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='user_review_job')
    is_liked = models.BooleanField()

    def __str__(self):
        return f"Review for {self.job_review} by {self.user}"

    class Meta:
        db_table = '"review"."job_review"'
        verbose_name = "Job_Review"
