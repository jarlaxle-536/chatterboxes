from django.urls import reverse

def get_talk_id(request):
    try:
        res = int(request.COOKIES.get('talk_id'))
    except Exception:
        res = None
    print(f'GET TALK ID RESULT: {res}, {type(res)}')
    return res

def is_chat_page(request):
    return request.path.startswith(reverse('chat'))
