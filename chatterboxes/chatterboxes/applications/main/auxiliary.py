from django.urls import reverse

from urllib.parse import urlencode, parse_qs

def get_talk_id(request):
    try:
        res = int(request.COOKIES.get('talk_id'))
    except Exception:
        res = None
    return res

def write_settings_to_cookies(
    response,
    settings_serializer,
    cookie_name='chat_settings'
    ):
    cookie_data = urlencode(settings_serializer.data)
    response.set_cookie(cookie_name, cookie_data)

def get_settings_from_cookies(
    response,
    cookie_name='chat_settings'
    ):
    acquired = {k: v[0] for k, v in
        parse_qs(response.cookies.get(cookie_name).coded_value).items()}
    print(sorted(acquired))
    return acquired

def get_chat_settings(request):
    res = request.COOKIES.get('chat_settings')
    return res

def is_chat_page(request):
    return request.path.startswith(reverse('chat'))
