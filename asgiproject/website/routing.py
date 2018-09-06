from django.urls import path
from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, ChannelNameRouter, URLRouter

from . import consumers

views_router = URLRouter([
    path('testhome/', consumers.BasicHttpConsumer)
])

websocket_router = AuthMiddlewareStack(
    URLRouter([
            url(r'^stream/$', consumers.StreamConsumer),
        ]
    )
)

beatserver_router = ChannelNameRouter({
    "testing-print": consumers.PrintConsumer
})