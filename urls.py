""" URLConf """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger import views
from messenger.chats.views import UserChatsViewSet
from messenger.groups.views import UserChatGroupsViewSet
from messenger.channels.views import UserChannelsViewSet

# Base router
router = DefaultRouter(trailing_slash=False)
router.register("users", views.UserViewSet, "user")
router.register("members", views.UserFilteredMemberViewSet, "member")
router.register("messages", views.UserFilteredMessageViewSet, "message")
router.register("reactions", views.UserFilteredReactionViewSet, "reaction")


urlpatterns = [
    # Users
    path("", include(router.urls)),
    # User Chats
    path(
        "users/<int:id>/chats/",
        UserChatsViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "users/<int:id>/chats/<int:pk>/",
        UserChatsViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    # User Groups
    path(
        "users/<int:id>/groups/",
        UserChatGroupsViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "users/<int:id>/groups/<int:pk>/",
        UserChatGroupsViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    # User Channels
    path(
        "users/<int:id>/channels/",
        UserChannelsViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "users/<int:id>/channels/<int:pk>/",
        UserChannelsViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    # Chats
    path("chats/", include("messenger.chats.urls")),
    # Groups
    path("groups/", include("messenger.groups.urls")),
    # Channels
    path("channels/", include("messenger.channels.urls")),
    # Message Reactions
    path(
        "messages/<int:id>/reactions/",
        views.MessageReactionsViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "messages/<int:id>/reactions/<int:pk>/",
        views.MessageReactionsViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
