from django.test import TestCase, tag
from http.cookies import SimpleCookie
from django.urls import reverse
from django.test import Client

@tag('views', 'main')
class MainPageAPIGetTest(TestCase):

    def setUp(self):
        self.url = reverse('main')
        self.client = Client()

    def test_get_without_cookies(self):
        response = self.client.get(self.url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.redirect_chain), 0)

    def test_get_with_valid_cookies(self):
        self.client.cookies = SimpleCookie({'talk_id': 1})
        response = self.client.get(self.url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertNotEquals(len(response.redirect_chain), 0)
        target_url = response.redirect_chain[-1][0]
        self.assertEquals(target_url, reverse('chat'))
