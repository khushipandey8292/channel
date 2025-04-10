"""
ASGI config for channelproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'channelproject.settings')
import channel_app.routing
import channel_layer_app.routing
application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':URLRouter(
        channel_app.routing.websocket_urlpatterns +
        channel_layer_app.routing.websocket_urlpatterns
    ),
})
