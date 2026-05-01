from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True