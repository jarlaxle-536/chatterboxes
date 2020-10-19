from rest_framework import serializers

class ChatSettingsSerializer(serializers.Serializer):
   allow_bots = serializers.BooleanField()
