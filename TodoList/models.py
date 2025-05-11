import uuid

from django.db import models

# Create your models here.
class Tasks(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default= uuid.uuid4)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    is_achieve = models.BooleanField(default=False)

    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title