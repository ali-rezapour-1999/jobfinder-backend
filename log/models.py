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

    class Meta:
        db_table = '"log"."error_log"'
        verbose_name = "error_log"
        verbose_name_plural = "error_log"


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

    class Meta:
        db_table = '"log"."rest_log"'
        verbose_name = "rest_log"
        verbose_name_plural = "rest_log"


class UserDeviceInfo(models.Model):
    ip_address = models.TextField(null=True , blank=True)
    user_agent = models.TextField()
    device_type = models.CharField(max_length=100, null=True, blank=True)
    browser = models.CharField(max_length=100, null=True, blank=True)
    os = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    screen_resolution =models.TextField(null=True, blank=True)
    timezone= models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.device} - {self.created_at}"

    class Meta:
        db_table = '"log"."user_device_info"'
        verbose_name = "UserDeviceInfo"
        verbose_name_plural = "UserDeviceInfo"
