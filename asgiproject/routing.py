from channels.routing import ProtocolTypeRouter

from asgiproject.website import routing

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'http': routing.views_router,
    'websocket': routing.websocket_router,
    'channel': routing.beatserver_router
})
