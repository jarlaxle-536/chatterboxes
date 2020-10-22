from django.test import TestCase, TransactionTestCase, tag
from django.contrib.sessions.models import Session
from django.urls import reverse
from django.test import Client

from chatterboxes.applications.main.models import *
from chatterboxes.applications.main.serializers import *

@tag('cookies')
class CookiesTest(TransactionTestCase):

    def setUp(self):
        for i in range(NUMBER_OF_CLIENTS):
            setattr(self, f'client{i + 1}', Client())

    def test_no_talk_id_in_pure_request(self):
        response = self.client1.get(reverse('main'))
        self.assertEquals(response.cookies.get('talk_id', None), None)
        print(Session.objects.all())

    def no_test_2(self):
        data = dict()
        response = self.client1.post(reverse('chat_settings'), data)
        print(response.content)
        data = CHAT_SETTINGS_VALID_DATA
        response = self.client1.post(reverse('chat_settings'), data, follow=True)
        print(response.content)

NUMBER_OF_CLIENTS = 5
CHAT_SETTINGS_VALID_DATA = {
    'allow_bots': False,
    'client_gender': 'male',
    'client_age': '0-15',
    'interlocutor_gender': 'male',
    'interlocutor_age': '0-15',
}
