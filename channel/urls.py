""" URLConf for channels app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.channel.views import (
    ChannelViewSet,
    ChannelMembersViewSet,
    ChannelMessagesViewSet,
)


router = DefaultRouter(trailing_slash=False)
router.register("", ChannelViewSet, "channel")


urlpatterns = [
    path("", include(router.urls)),
    # Channel members
    path(
        "<int:id>/members/",
        ChannelMembersViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "<int:id>/members/<int:pk>/",
        ChannelMembersViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    # Channel messages
    path(
        "<int:id>/messages/",
        ChannelMessagesViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "<int:id>/messages/<int:pk>/",
        ChannelMessagesViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
