from django.test import TestCase, TransactionTestCase, tag
from django.contrib.sessions.models import Session
from http.cookies import SimpleCookie
from django.core.cache import cache
from django.urls import reverse
from django.test import Client

from chatterboxes.applications.main.models import *
from chatterboxes.applications.main.serializers import *

@tag('views', 'main')
class MainPageAPITest(TransactionTestCase):

    def setUp(self):
        self.url = reverse('main')
        self.client = Client()

    def test_get_no_cookies(self):
        response = self.client.get(self.url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.redirect_chain), 0)
        print(response.cookies)

    def test_get_with_cookies(self):
        self.client.cookies = SimpleCookie({'talk_id': 1})
        response = self.client.get(self.url, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertNotEquals(len(response.redirect_chain), 0)
        target_url = response.redirect_chain[-1][0]
        self.assertEquals(target_url, reverse('chat'))
        print(response.cookies)
