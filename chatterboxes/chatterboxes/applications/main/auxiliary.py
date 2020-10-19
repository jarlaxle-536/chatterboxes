from django.urls import reverse

def get_talk_id(request):
    res = request.COOKIES.get('talk_id')
    print(f'GET TALK ID RESULT: {res}, {type(res)}')
    return res

def is_chat_page(request):
    return request.path.startswith(reverse('chat'))
