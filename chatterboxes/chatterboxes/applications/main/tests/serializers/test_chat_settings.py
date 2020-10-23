from django.test import TestCase, TransactionTestCase, tag

from chatterboxes.applications.main.models import *
from chatterboxes.applications.main.serializers import *

@tag('serializer', 'settings')
class ChatSettingsSerializationTest(TransactionTestCase):

    def setUp(self):
        self.default_object = ChatSettings.default_object()

    def test_default(self):
        serializer = ChatSettingsSerializer(self.default_object)
        for k, v in serializer.data.items():
            self.assertEquals(v, getattr(self.default_object, k))

@tag('serializer', 'settings')
class ChatSettingsDeserializationTest(TransactionTestCase):

    def setUp(self):
        pass

    def test_all_valid(self):
        serializer = ChatSettingsSerializer(data=VALID_SETTINGS_SERIALIZER_DATA)
        self.assertTrue(serializer.is_valid())

    def test_smth_invalid(self):
        for k, v in INVALID_SETTINGS_SERIALIZER_DATA.items():
            data = VALID_SETTINGS_SERIALIZER_DATA.copy()
            data[k] = v
            serializer = ChatSettingsSerializer(data=data)
            self.assertFalse(serializer.is_valid())

VALID_SETTINGS_SERIALIZER_DATA = {
    'allow_bots': False,
    'client_gender': 'male',
    'client_age': '0-15',
    'interlocutor_gender': ['male', 'female'],
    'interlocutor_age': ['0-15'],
}

INVALID_SETTINGS_SERIALIZER_DATA = {
    'allow_bots': None,
    'client_gender': None,
    'client_age': None,
    'interlocutor_gender': 'male',
    'interlocutor_age': '0-15',
}
