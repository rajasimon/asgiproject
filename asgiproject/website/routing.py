from django.conf.urls import url
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, ChannelNameRouter, URLRouter

from . import views
from . import consumers

views_router = URLRouter([
    url(r"^$", views.BasicHttpConsumer)
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