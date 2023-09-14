""" URLConf for groups app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.groups.views import (
    ChatGroupViewSet,
    ChatGroupMembersViewSet,
    ChatGroupMessagesViewSet,
)


router = DefaultRouter(trailing_slash=False)
router.register("", ChatGroupViewSet, "chatgroup")


urlpatterns = [
    path("", include(router.urls)),
    # Group members
    path(
        "<int:id>/members/",
        ChatGroupMembersViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "<int:id>/members/<int:pk>/",
        ChatGroupMembersViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    # Group messages
    path(
        "<int:id>/messages/",
        ChatGroupMessagesViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "<int:id>/messages/<int:pk>/",
        ChatGroupMessagesViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
