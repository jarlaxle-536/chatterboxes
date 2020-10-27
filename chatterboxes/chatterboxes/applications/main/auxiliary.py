from django.urls import reverse

from urllib.parse import urlencode, parse_qs
import json

from .serializers import *

def get_talk_id(request):
    try:
        res = int(request.COOKIES.get('talk_id'))
    except Exception:
        res = None
    return res

def get_settings_from_request(request):
    return request.COOKIES.get('chat_settings')

def write_settings_to_cookies(
    response,
    settings_serializer,
    cookie_name='chat_settings'
    ):
    try:
        serializer_data = {k:v for k, v in settings_serializer.data.items()}
        for key in ['interlocutor_age', 'interlocutor_gender']:
            serializer_data[key] = list(serializer_data[key])
        cookie_data = urlencode(serializer_data)
        response.set_cookie(cookie_name, cookie_data)
    except Exception:
        pass

def get_settings_from_cookies(
    response,
    cookie_name='chat_settings'
    ):
    try:
        data = {k.replace('\"', ''): v[0] for k, v in
            parse_qs(response.cookies.get(cookie_name).coded_value).items()}
        for key in ['interlocutor_age', 'interlocutor_gender']:
            for r in '[]\'':
                data[key] = data[key].replace(r, '')
            data[key] = set(data[key].split(', '))
        data['allow_bots'] = {str(b): b for b in [True, False]}.get(
            data['allow_bots'].replace('\"', ''))
    except Exception:
        data = {k: None for k in ChatSettingsSerializer._declared_fields}
        data['allow_bots'] = False
    return data

def is_chat_page(request):
    return request.path.startswith(reverse('chat'))
