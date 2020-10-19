from rest_framework import serializers
from django.conf import settings

class Settings:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

class ChatSettingsSerializer(serializers.Serializer):
    client_gender = serializers.ChoiceField(
        choices=settings.GENDERS,
        style={'base_template': 'radio.html'}
    )
    client_age = serializers.ChoiceField(
        choices=settings.AGES,
        style={'base_template': 'radio.html'}
    )
    interlocutor_gender = serializers.MultipleChoiceField(
        choices=settings.GENDERS,
    )
    interlocutor_age = serializers.MultipleChoiceField(
        choices=settings.AGES,
    )
    allow_bots = serializers.BooleanField()

    def create(self, validated_data):
        return Settings(**validated_data)
