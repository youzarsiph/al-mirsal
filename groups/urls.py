""" URLConf for messenger.groups """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.groups.views import GroupViewSet
from messenger.links.views import GroupLinkViewSet
from messenger.members.views import GroupMembersViewSet
from messenger.msgs.views import GroupMessagesViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("groups", GroupViewSet, "group")

sub_router = DefaultRouter()
sub_router.register("links", GroupLinkViewSet, "link")
sub_router.register("members", GroupMembersViewSet, "member")
sub_router.register("messages", GroupMessagesViewSet, "message")

urlpatterns = [
    path("", include(router.urls)),
    # Group invite links, members and messages
    path(
        "groups/<int:id>/",
        include((sub_router.urls, "groups"), namespace="groups"),
    ),
]
