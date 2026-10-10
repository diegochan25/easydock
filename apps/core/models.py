from django.db import models

class SampleWord(models.Model):
    class PartsOfSpeech(models.TextChoices):
        NOUN = 'noun'
        ADJECTIVE = 'adjective'

    id = models.BigAutoField(primary_key=True)
    word = models.CharField(max_length=255)
    part_of_speech = models.CharField(max_length=64, choices=PartsOfSpeech.choices, db_index=True)

    # Annotations
    objects: 'models.Manager[SampleWord]'

    @classmethod
    def random_name(cls) -> str:
        adj = cls.objects.filter(part_of_speech=cls.PartsOfSpeech.ADJECTIVE).order_by('?').first().word
        noun = cls.objects.filter(part_of_speech=cls.PartsOfSpeech.NOUN).order_by('?').first().word
        return f"{adj}-{noun}"