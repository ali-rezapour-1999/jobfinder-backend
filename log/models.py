from django.db import models
from django.utils.timezone import now

from user.models import CustomUser


class ErrorLog(models.Model):
    timestamp = models.DateTimeField(default=now)
    message = models.TextField()
    level = models.CharField(max_length=50)
    logger = models.CharField(max_length=255)
    traceback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"[{self.level}] {self.message[:50]}"


class RestLog(models.Model):
    timestamp = models.DateTimeField(default=now)
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True
    )
    method = models.CharField(max_length=10)
    path = models.CharField(max_length=255)
    status_code = models.IntegerField()
    response_time = models.FloatField(help_text="Time in seconds")

    def __str__(self):
        return f"{self.method} {self.path} ({self.status_code})"
