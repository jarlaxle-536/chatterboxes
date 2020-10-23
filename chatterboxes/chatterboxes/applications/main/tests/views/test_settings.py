from django.test import TestCase, tag
from http.cookies import SimpleCookie
from django.urls import reverse
from django.test import Client

@tag('views', 'settings')
class SettingsAPITest(TestCase):

    def setUp(self):
        self.url = reverse('chat_settings')

    def test_get_without_cookies(self):
        response = self.client.get(self.url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.redirect_chain), 0)
        serializer_key = 'chat_settings_serializer'
        serializer = response.context.get(serializer_key)
        self.assertTrue(serializer is not None)
        print(serializer.data)

    def no_test_get_with_cookies(self):
        self.client.cookies = SimpleCookie({'talk_id': 1})
        response = self.client.get(self.url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertNotEquals(len(response.redirect_chain), 0)
        target_url = response.redirect_chain[-1][0]
        self.assertEquals(target_url, reverse('chat'))
