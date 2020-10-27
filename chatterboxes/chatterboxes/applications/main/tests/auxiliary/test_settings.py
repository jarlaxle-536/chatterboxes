from django.test import TestCase, RequestFactory, tag
from django.urls import reverse

from chatterboxes.applications.main.serializers import *
from chatterboxes.applications.main.auxiliary import *
from chatterboxes.applications.main.models import *

@tag('auxiliary', 'settings', 'settings_auxiliary')
class ResponseSettingsTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('chat_settings'), follow=True)

    def test_set_and_get_the_same(self):
        for obj in SETTINGS_OBJECTS:
            serializer = ChatSettingsSerializer(obj)
            write_settings_to_cookies(self.response, serializer)
            acquired_data = get_settings_from_cookies(self.response)
            self.assertEquals(serializer.data, acquired_data)

SETTINGS_OBJECTS = [
    None,
    ChatSettings.default_object(),
]

COOKIES = [
    dict(),
    {'talk_id': 1},
    {'talk_id': None},
    {'talk_id': 'FAIL'},
]
