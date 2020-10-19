from rest_framework import serializers

class ChatSettingsSerializer(serializers.Serializer):
    client_gender = serializers.ChoiceField(
        choices=['male', 'female'],
        style={'base_template': 'radio.html'}
    )
    client_age = serializers.ChoiceField(
        choices=['0-15', '15-25', '25-55', '55-100'],
        style={'base_template': 'radio.html'}
    )
    interlocutor_gender = serializers.ChoiceField(
        choices=['male', 'female'],
        style={'base_template': 'radio.html'}
    )
    interlocutor_age = serializers.ChoiceField(
        choices=['0-15', '15-25', '25-55', '55-100'],
        style={'base_template': 'radio.html'}
    )
    allow_bots = serializers.BooleanField()
