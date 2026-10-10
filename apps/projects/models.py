from typing import TYPE_CHECKING
from django.conf import settings
from django.db import models

if TYPE_CHECKING:
    from django.db.models.fields.related_descriptors import RelatedManager
    from apps.services.models import Service

class Project(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=128)
    description = models.TextField(null=True)

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='created_projects', on_delete=models.SET_NULL)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owned_projects', on_delete=models.RESTRICT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Annotations
    objects: 'models.Manager[Project]'
    services: 'RelatedManager[Service]'

    class Meta:
        db_table = 'projects'