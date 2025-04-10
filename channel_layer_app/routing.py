from django.urls import path
from .import consumers

websocket_urlpatterns= [
    path('room1/sc/<str:groupkaname>/',consumers.RoomSyncConsumer.as_asgi()),
]