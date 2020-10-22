from rest_framework import serializers
from django.conf import settings

from .models import *

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
    allow_bots = serializers.BooleanField(

    )

    def create(self, validated_data):
        return ChatSettings(**validated_data)

class ChatSettings:
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)

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
#    def save(self):
#        print(f'saving {self}')
#        print(self.validated_data)
#        for k, v in self.validated_data.items():
#            print(k, v)
#            setattr(self, k, v)
#        for k, v in kwargs['data'].items():
#            setattr(self, k, v)
#        return super().save()
