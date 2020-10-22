from django.db import models

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
