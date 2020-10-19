from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

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
        data = {'allow_bots': False}
        context = {
            'chat_settings_form': ChatSettingsSerializer(data),
        }
        return Response(context)
