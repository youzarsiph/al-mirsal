""" URLConf for messenger.channels """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.urls import actions
from messenger.channels.views import ChannelViewSet
from messenger.links.views import ChannelLinkViewSet
from messenger.members.views import ChannelMembersViewSet
from messenger.msgs.views import ChannelMessagesViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("", ChannelViewSet, "channel")


urlpatterns = [
    path("", include(router.urls)),
    # Channel invite links
    path(
        "<int:id>/links/",
        ChannelLinkViewSet.as_view(actions["list_create"]),
    ),
    path(
        "<int:id>/links/<int:pk>/",
        ChannelLinkViewSet.as_view(actions["retrieve_update_destroy"]),
    ),
    # Channel members
    path(
        "<int:id>/members/",
        ChannelMembersViewSet.as_view(actions["list_create"]),
    ),
    path(
        "<int:id>/members/<int:pk>/",
        ChannelMembersViewSet.as_view(actions["retrieve_update_destroy"]),
    ),
    # Channel messages
    path(
        "<int:id>/messages/",
        ChannelMessagesViewSet.as_view(actions["list_create"]),
    ),
    path(
        "<int:id>/messages/<int:pk>/",
        ChannelMessagesViewSet.as_view(actions["retrieve_update_destroy"]),
    ),
]
