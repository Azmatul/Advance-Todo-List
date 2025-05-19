import uuid
from django.db import models
from django.conf import settings

class Tasks(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    is_achieve = models.BooleanField(default=False)
    create_at = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        verbose_name_plural = "Tasks"
        ordering = ['-create_at']

    def __str__(self):
        return f"{self.title} (by {self.created_by.email if self.created_by_id else 'deleted-user'})"