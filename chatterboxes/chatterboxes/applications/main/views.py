from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect

from .serializers import *

class MainPageAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main_page.html'
    def get(self, request):
        return Response()

class SettingsAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat_settings.html'

    def get(self, request):
        data = {
            'allow_bots': False,
            'client_gender': 'male',
            'client_age': '0-15',
            'interlocutor_gender': 'male',
            'interlocutor_age': '0-15',
        }
        context = {
            'chat_settings_form': ChatSettingsSerializer(data),
        }
        return Response(context)

    def post(self, request):
        print(request.POST)
        serializer = ChatSettingsSerializer(data=request.POST)
        print(serializer)
        if serializer.is_valid():
            print('VALID')
        context = {
            'chat_settings_form': serializer,
        }
        return redirect('chat')

class ChatAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chat.html'
    def get(self, request):
        return Response()
