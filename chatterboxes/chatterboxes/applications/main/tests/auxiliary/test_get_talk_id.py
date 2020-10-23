from django.test import TestCase, RequestFactory, tag
from django.urls import reverse

from chatterboxes.applications.main.auxiliary import *

@tag('auxiliary', 'get_talk_id')
class GetCorrectTalkIdTest(TestCase):

    def test_get_talk_id(self):
        for cookie_dict in COOKIES:
            request = RequestFactory().get(reverse('main'))
            request.COOKIES.update(cookie_dict)
            acquired_talk_id = get_talk_id(request)
            self.assertIn(acquired_talk_id,
                [cookie_dict.get('talk_id', None), None])

COOKIES = [
    dict(),
    {'talk_id': 1},
    {'talk_id': None},
    {'talk_id': 'FAIL'},
]
