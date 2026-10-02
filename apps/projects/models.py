from uuid import uuid4
from django.db import models


class Project(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)

    name = models.CharField(max_length=128)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)