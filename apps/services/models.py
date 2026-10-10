from django.db import models


class Service(models.Model):
    class Types(models.TextChoices):
        BUCKET = ('bucket', 'Bucket')
        DATABASE = ('database', 'Database')
        DOCKER_IMAGE = ('docker_image', 'Docker image')
        FUNCTION = ('function', 'Function')
        GITHUB_REPOSITORY = ('github_repository', 'GitHub repository')

    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=128)
    type = models.CharField(max_length=255, choices=Types.choices)

    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='services')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Annotations
    objects: 'models.Manager[Service]'

    class Meta:
        db_table = 'services'


class Volume(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Annotations
    objects: 'models.Manager[Volume]'


class VolumeBinding(models.Model):
    pk = models.CompositePrimaryKey('volume', 'service')
    volume = models.ForeignKey('Volume', on_delete=models.CASCADE, db_index=True)
    service =  models.ForeignKey('Service', on_delete=models.CASCADE, db_index=True)

    # Annotations
    objects: 'models.Manager[VolumeBinding]'

    class Meta:
        db_table = 'volume_bindings'

class Bucket(models.Model):
    id = models.BigAutoField(primary_key=True)

    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    # Annotations
    objects: 'models.Manager[Bucket]'
    service_id: int

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'buckets'