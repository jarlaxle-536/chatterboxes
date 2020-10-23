from django.urls import reverse

def get_talk_id(request):
    try:
        res = int(request.COOKIES.get('talk_id'))
    except Exception:
        res = None
    return res

def get_chat_settings(request):
    res = request.COOKIES.get('chat_settings')
    return res

def is_chat_page(request):
    return request.path.startswith(reverse('chat'))
