from rest_framework import serializers
from django.conf import settings

from .models import *

class ChatSettingsSerializer(serializers.Serializer):
    client_gender = serializers.ChoiceField(
        choices=settings.GENDERS,
        default=settings.DEFAULT_GENDER,
        style={'base_template': 'radio.html'}
    )
    client_age = serializers.ChoiceField(
        choices=settings.AGES,
        default=settings.DEFAULT_AGE,
        style={'base_template': 'radio.html'},
    )
    interlocutor_gender = serializers.MultipleChoiceField(
        choices=settings.GENDERS,
        default=[settings.DEFAULT_GENDER],
    )
    interlocutor_age = serializers.MultipleChoiceField(
        choices=settings.AGES,
        default=[settings.DEFAULT_AGE],
    )
    allow_bots = serializers.BooleanField(
        default=False,
    )

    def create(self, validated_data):
        print(f'calling settings_serializer create with {self}, {validated_data}')
        result = ChatSettings(**validated_data)
        print(f'result: {result}')
        return result

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['text', 'talk_id']
    def create(self, validated_data):
        print('message serializer create')
        return ChatMessage.objects.create(**validated_data)
    def update(self, inst, validated_data):
        for k, v in validated_data.items():
            setattr(inst, k, v)
        inst.save()
        return inst

class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ['has_ended']
    def create(self, validated_data):
        print('talk serializer create')
        print(validated_data)
        talk = Talk.objects.create(**validated_data)
        print(talk.__dict__)
        return talk
    def update(self, inst, validated_data):
        print(f'calling update on {inst} with {validated_data}')
        for k, v in validated_data.items():
            setattr(inst, k, v)
        inst.save()
        return inst
