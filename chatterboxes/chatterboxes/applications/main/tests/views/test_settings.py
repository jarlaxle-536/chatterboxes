from django.test import TestCase, TransactionTestCase, tag
from django.contrib.sessions.models import Session
from django.urls import reverse
from django.test import Client

from chatterboxes.applications.main.models import *
from chatterboxes.applications.main.serializers import *

@tag('views')
class SettingsAPITest(TransactionTestCase):

    def setUp(self):
        for i in range(NUMBER_OF_CLIENTS):
            setattr(self, f'client{i + 1}', Client())

NUMBER_OF_CLIENTS = 5
