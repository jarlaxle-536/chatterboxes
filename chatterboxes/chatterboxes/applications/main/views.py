from django.http import HttpResponse
from django.template import loader

from .forms import *

def main(request):
    template = loader.get_template('main_page.html')
    context = dict()
    return HttpResponse(template.render(context, request))

def settings(request):
    """Works with settings form"""
    template = loader.get_template('chat_settings.html')
    context = dict()
    context['chat_settings_form'] = ChatSettingsForm()
    return HttpResponse(template.render(context, request))
