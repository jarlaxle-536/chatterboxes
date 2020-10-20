from channels.routing import ProtocolTypeRouter, URLRouter
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
#from channels.auth import AuthMiddlewareStack

import chatterboxes.applications.main.channel_routes

application = ProtocolTypeRouter({
    'websocket': URLRouter(
        chatterboxes.applications.main.channel_routes.urlpatterns
    )
})
