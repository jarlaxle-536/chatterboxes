from django.test import TestCase, tag

from chatterboxes.applications.main.models import *
from chatterboxes.applications.main.serializers import *

@tag('serializer', 'settings')
class ChatSettingsSerializationTest(TestCase):

    def setUp(self):
        self.default_object = ChatSettings.default_object()

    def test_default(self):
        serializer = ChatSettingsSerializer(self.default_object)
        for k, v in serializer.data.items():
            self.assertEquals(v, getattr(self.default_object, k))

@tag('serializer', 'settings')
class ChatSettingsDeserializationTest(TestCase):
    
    def test_all_valid(self):
        serializer = ChatSettingsSerializer(data=VALID_SETTINGS_SERIALIZER_DATA)
        self.assertTrue(serializer.is_valid())

    def test_smth_invalid(self):
        for k, v in INVALID_SETTINGS_SERIALIZER_DATA.items():
            data = VALID_SETTINGS_SERIALIZER_DATA.copy()
            data[k] = v
            serializer = ChatSettingsSerializer(data=data)
            self.assertFalse(serializer.is_valid())

CHAT_SETTINGS_DEFAULT = ChatSettings.default_object()

VALID_SETTINGS_SERIALIZER_DATA = CHAT_SETTINGS_DEFAULT.__dict__

INVALID_SETTINGS_SERIALIZER_DATA = {k: None
    for k in CHAT_SETTINGS_DEFAULT.__dict__}
