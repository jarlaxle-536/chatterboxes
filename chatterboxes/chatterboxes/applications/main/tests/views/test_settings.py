from django.test import TestCase, tag
from http.cookies import SimpleCookie
from django.urls import reverse
from django.test import Client

from urllib.parse import urlencode, parse_qs
import json

from chatterboxes.applications.main.auxiliary import *
from chatterboxes.applications.main.models import *

@tag('views', 'settings', 'settings_views')
class SettingsAPIGetTest(TestCase):

    def setUp(self):
        self.url = reverse('chat_settings')
        self.serializer_key = 'chat_settings_serializer'

    def test_get_without_cookies(self):
        response = self.client.get(self.url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.redirect_chain), 0)
        serializer = response.context.get(self.serializer_key)
        self.assertTrue(serializer is not None)
        self.assertEquals(serializer.data,
            ChatSettings.default_object().__dict__)

    def test_get_with_valid_cookies(self):
        self.client.cookies = SimpleCookie({'talk_id': 1})
        response = self.client.get(self.url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertNotEquals(len(response.redirect_chain), 0)
        target_url = response.redirect_chain[-1][0]
        self.assertEquals(target_url, reverse('chat'))
        serializer = response.context.get(self.serializer_key, None)
        self.assertTrue(serializer is None)

@tag('views', 'settings', 'settings_views')
class SettingsAPIPostTest(TestCase):

    def setUp(self):
        self.url = reverse('chat_settings')

    def test_post(self):
        default_data = ChatSettings.default_object().__dict__
        response = self.client.post(self.url, default_data, follow=True)
        'ensure this provided data is stored in cookies'
        print('response cookies:', response.cookies)
        print('chat settings:', response.cookies.get('chat_settings'))
        res = get_settings_from_cookies(response)
#        res = parse_qs(response.cookies.get('chat_settings').coded_value)
#        res = json.loads(response.cookies.get('chat_settings').coded_value)
        print(res, type(res))

#        res = json.loads(response.cookies.get('chat_settings'))
#        print(res)
