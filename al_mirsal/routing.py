""" Channels Routing """

from django.urls import path, re_path

from al_mirsal.channel.consumers import ChannelMessageConsumer
from al_mirsal.chats.consumers import ChatMessageConsumer
from al_mirsal.consumers import MainConsumer
from al_mirsal.groups.consumers import GroupMessageConsumer


# Create your routing here.
ws_urlpatterns = [
    path(r"ws/", MainConsumer.as_asgi()),
    re_path(r"ws/channels/(?P<id>\w+)/$", ChannelMessageConsumer.as_asgi()),
    re_path(r"ws/chats/(?P<id>\w+)/$", ChatMessageConsumer.as_asgi()),
    re_path(r"ws/groups/(?P<id>\w+)/$", GroupMessageConsumer.as_asgi()),
]
