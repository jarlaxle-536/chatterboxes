from django.test import TestCase, TransactionTestCase, tag

from chatterboxes.applications.main.models import *
from chatterboxes.applications.main.serializers import *

@tag('serializer')
class ChatMessageSerializerTest(TransactionTestCase):

    def setUp(self):
        pass

    def test_1(self):
        pass
