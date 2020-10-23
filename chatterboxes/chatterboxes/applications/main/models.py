from django.db import models

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
