from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

import json

from .models import *

class GeneralConsumer(WebsocketConsumer):

    group_name = 'general'

    def connect(self):
        print(f'{self.group_name} connect')
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name)

    def disconnect(self, close_code):
        print(f'{self.group_name} disconnect')
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name)

    def general_add(self, kwargs):
        print(f'general add with {kwargs}')
        self.send('lorem')

class ChatConsumer(WebsocketConsumer):

    group_name = 'chat'

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name)

    def chat_update(self, kwargs):
        text = json.dumps(kwargs['serializer_data'])
        self.send(text)
