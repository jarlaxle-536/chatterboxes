from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from http.cookies import SimpleCookie
from django.shortcuts import redirect

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


from .serializers import *
from .auxiliary import *
from .models import *

class MainPageAPI(APIView):

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_page.html'

    def get(self, request):

        print('main:get')
        talk_id = get_talk_id(request)
        print(f'cookies: {request.COOKIES}')
        print(f'talk id: {talk_id}')
        if talk_id is None:
            return Response()
        else:
            return redirect('chat')

class SettingsAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat_settings.html'

    def get(self, request):
        print('chat_settings:get')
        data = {
            'allow_bots': False,
            'client_gender': 'male',
            'client_age': '0-15',
            'interlocutor_gender': 'male',
            'interlocutor_age': '0-15',
        }
        context = {
            'chat_settings_serializer': ChatSettingsSerializer(data),
        }
        return Response(context)

    def post(self, request):
        print('chat_settings:post')
        serializer = ChatSettingsSerializer(data=request.POST)
        print(serializer)
        if serializer.is_valid():
            print('VALID')
            "save settings to cookies!"
        else:
            print('INVALID')
            print(serializer.errors)
        context = {
            'chat_settings_serializer': serializer,
        }
        'search for possible interlocutor here'
        return redirect('chat')

class ChatAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat.html'

    def get(self, request):
        print('chat:get')
        talk_id = get_talk_id(request)
        talk, created = Talk.objects.get_or_create(pk=talk_id)
        data = {'text': ''}
        context = {
            'talk': talk,
            'chat_message_serializer': ChatMessageSerializer(data),
        }
        response = Response(context)
        response.set_cookie('talk_id', talk.id)
        return response

    def post(self, request):
        print('chat:post')
        serializer = ChatMessageSerializer(data=request.POST)
        if serializer.is_valid():
            print('VALID')
            serializer.save(talk_id=get_talk_id(request))
        else:
            print('INVALID')
            print(serializer.errors)
        context = {
            'chat_message_serializer': serializer,
        }
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
        'chat', {
            'type': 'chat.update',
            'serializer_data': serializer.data
            }
        )
        return Response(context)

    def patch(self, request):
        print('chat:patch')
        print(request.COOKIES)
        print(request.data)
        talk_id = get_talk_id(request)
        talk = Talk.objects.get(pk=talk_id)
        data = {'text': ''}
        talk_serializer = TalkSerializer(data=request.data)
        print(talk_serializer)
        if talk_serializer.is_valid():
            print(talk, talk.__dict__)
            print('VALID')
            talk = talk_serializer.save()
            print(talk, talk.__dict__)
        else:
            print(talk_serializer.errors)
        context = {
            'talk': talk,
            'chat_message_serializer': ChatMessageSerializer(data),
        }
        response = Response(context)
#        response.set_cookie('talk_id', None) # resetting cookies
        return response
