from django.test import TestCase, TransactionTestCase, tag
from django.contrib.sessions.models import Session
from channels.layers import get_channel_layer
from django.core.cache import cache
from django.urls import reverse
from django.test import Client

from chatterboxes.applications.main.models import *
from chatterboxes.applications.main.serializers import *

@tag('views')
class MainPageAPITest(TransactionTestCase):

    def setUp(self):
        self.url = reverse('main')
        for i in range(NUMBER_OF_CLIENTS):
            setattr(self, f'client{i + 1}', Client())

    def test_get(self):
        'as if user enters site for the first time'
        response = self.client1.get(self.url)
        channel_layer = get_channel_layer()
        print(response.data)
        print(channel_layer)
        print(response.request)
#        request.session.get('talk_id', None)

NUMBER_OF_CLIENTS = 5
