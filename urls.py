""" URLConf for messenger """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.views import UserViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)

actions = {
    "list_create": {"get": "list", "post": "create"},
    "retrieve_update_destroy": {
        "get": "retrieve",
        "delete": "destroy",
        "put": "update",
        "patch": "partial_update",
    },
}

urlpatterns = [
    # Users
    path("", include(router.urls)),
    path("users/<int:pk>/", UserViewSet.as_view(actions["retrieve_update_destroy"])),
    # Channels
    path("channels/", include("messenger.channels.urls")),
    # Chats
    path("chats/", include("messenger.chats.urls")),
    # Forwards
    path("forwards/", include("messenger.forwards.urls")),
    # Groups
    path("groups/", include("messenger.groups.urls")),
    # Links
    path("links/", include("messenger.links.urls")),
    # Members
    path("members/", include("messenger.members.urls")),
    # Messages
    path("messages/", include("messenger.msgs.urls")),
    # Reactions
    path("reactions/", include("messenger.reactions.urls")),
    # Stories
    path("stories/", include("messenger.stories.urls")),
]
