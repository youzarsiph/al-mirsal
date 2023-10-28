""" URLConf for messenger.groups """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.urls import actions
from messenger.groups.views import GroupViewSet
from messenger.links.views import GroupLinkViewSet
from messenger.members.views import GroupMembersViewSet
from messenger.msgs.views import GroupMessagesViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("", GroupViewSet, "group")


urlpatterns = [
    path("", include(router.urls)),
    # Group invite links
    path(
        "<int:id>/links/",
        GroupLinkViewSet.as_view(actions["list_create"]),
    ),
    path(
        "<int:id>/links/<int:pk>/",
        GroupLinkViewSet.as_view(actions["retrieve_update_destroy"]),
    ),
    # Group members
    path(
        "<int:id>/members/",
        GroupMembersViewSet.as_view(actions["list_create"]),
    ),
    path(
        "<int:id>/members/<int:pk>/",
        GroupMembersViewSet.as_view(actions["retrieve_update_destroy"]),
    ),
    # Group messages
    path(
        "<int:id>/messages/",
        GroupMessagesViewSet.as_view(actions["list_create"]),
    ),
    path(
        "<int:id>/messages/<int:pk>/",
        GroupMessagesViewSet.as_view(actions["retrieve_update_destroy"]),
    ),
]
