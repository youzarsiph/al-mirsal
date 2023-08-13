""" URLConf for groups app """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.groups.views import (
    GroupViewSet,
    GroupMembersViewSet,
    GroupMessagesViewSet,
)


router = DefaultRouter(trailing_slash=False)
router.register("", GroupViewSet, "chatgroup")


urlpatterns = [
    path("", include(router.urls)),
    # Group members
    path(
        "<int:id>/members/",
        GroupMembersViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "<int:id>/members/<int:pk>/",
        GroupMembersViewSet.as_view(
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
        GroupMessagesViewSet.as_view({"get": "list", "post": "create"}),
    ),
    path(
        "<int:id>/messages/<int:pk>/",
        GroupMessagesViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
]
