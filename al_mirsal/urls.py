""" URLConf for al_mirsal """

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from al_mirsal.channel.views import ChannelViewSet
from al_mirsal.chats.views import ChatViewSet
from al_mirsal.groups.views import GroupViewSet
from al_mirsal.members.views import MemberViewSet
from al_mirsal.messages.views import MessageViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("channels", ChannelViewSet, "channel")
router.register("chats", ChatViewSet, "chat")
router.register("groups", GroupViewSet, "group")
router.register("members", MemberViewSet, "member")
router.register("messages", MessageViewSet, "message")


urlpatterns = [
    path("", include(router.urls)),
]
