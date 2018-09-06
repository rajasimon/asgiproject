from django.urls import path, re_path
from django.conf.urls import url
from django.contrib import admin

from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, ChannelNameRouter, URLRouter

from . import consumers

views_router = URLRouter([
    path('', consumers.BasicHttpConsumer),
    re_path("^", AsgiHandler),
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