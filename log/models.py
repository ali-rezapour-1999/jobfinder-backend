from django.db import models

from user.models import CustomUser


class ErrorLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True
    )
    error_message = models.TextField()
    stack_trace = models.TextField(blank=True, null=True)
    request_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Error at {self.timestamp}: {self.error_message[:40]}"


class RestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.SET_NULL, null=True, blank=True
    )
    action = models.CharField(max_length=255)
    request_data = models.JSONField(blank=True, null=True)
    response_data = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"Action: {self.action} at {self.timestamp}"
