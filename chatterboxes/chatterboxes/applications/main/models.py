from django.conf import settings
from django.db import models

class ChatSettings:
    '*Not a model'
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def default_object(cls):
        return cls(
            client_gender=settings.DEFAULT_GENDER,
            client_age=settings.DEFAULT_AGE,
            interlocutor_gender=set([settings.DEFAULT_GENDER]),
            interlocutor_age=set([settings.DEFAULT_AGE]),
            allow_bots=False
        )

class ChatSession(models.Model):
    identifier = models.CharField(max_length=50)
    class Meta:
        abstract = True

class ChatMessage(models.Model):
    text = models.TextField()
    talk = models.ForeignKey(
        'Talk',
        on_delete=models.CASCADE,
    )

class Talk(models.Model):
    has_ended = models.BooleanField(
        default=False
    )
