from channels.generic.websocket import WebsocketConsumer
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from .models import *

class ChatConsumer(WebsocketConsumer):

    group_name = 'chat'

    def connect(self):
        self.accept()
        async_to_sync(self.channel_layer.group_add)(
            self.group_name, self.channel_name)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name)
