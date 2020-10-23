from django.test import TestCase, TransactionTestCase, tag
from django.contrib.sessions.models import Session
from django.urls import reverse
from django.test import Client

from chatterboxes.applications.main.models import *
from chatterboxes.applications.main.serializers import *

@tag('views')
class SettingsAPITest(TransactionTestCase):

    def setUp(self):
        self.url = reverse('chat_settings')
        for i in range(NUMBER_OF_CLIENTS):
            setattr(self, f'client{i + 1}', Client())

    def test_get(self):
        'as if user enters site for the first time'
        response = self.client1.get(self.url)
        print(response.cookies)
#        request.session.get('talk_id', None)


NUMBER_OF_CLIENTS = 5