""" URLConf for messenger.channels """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.channels.views import ChannelViewSet
from messenger.links.views import ChannelLinkViewSet
from messenger.msgs.views import ChannelMessagesViewSet
from messenger.subscribers.views import ChannelSubscribersViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("channels", ChannelViewSet, "channel")

sub_router = DefaultRouter()
sub_router.register("links", ChannelLinkViewSet, "link")
sub_router.register("messages", ChannelMessagesViewSet, "message")
sub_router.register("subscribers", ChannelSubscribersViewSet, "subscriber")

urlpatterns = [
    path("", include(router.urls)),
    # Channel invite links, members and messages
    path(
        "channels/<int:id>/",
        include((sub_router.urls, "channels"), namespace="channels"),
    ),
]
