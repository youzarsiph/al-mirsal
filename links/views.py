""" API endpoints for messenger.links """


import secrets
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.channels.models import Channel
from messenger.channels.permissions import IsChannelMember
from messenger.groups.models import Group
from messenger.groups.permissions import IsGroupMember
from messenger.links.models import Link
from messenger.links.serializers import LinkSerializer


# Create your views here.
class LinkViewSet(ModelViewSet):
    """Create, read, update and delete Invite Links"""

    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [IsAuthenticated]


class UserLinksViewSet(OwnerMixin, LinkViewSet):
    """User invite links"""

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)


class ChannelLinkViewSet(LinkViewSet):
    """Channel invite links"""

    permission_classes = [IsAuthenticated, IsChannelMember]

    def perform_create(self, serializer):
        channel = Channel.objects.get(pk=self.kwargs["id"])
        serializer.save(
            channel=channel,
            user=self.request.user,
            token=secrets.token_urlsafe(7),
        )

    def get_queryset(self):
        """Filter queryset by channel"""

        channel = Channel.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(channel=channel)


class GroupLinkViewSet(LinkViewSet):
    """Group invite links"""

    permission_classes = [IsAuthenticated, IsGroupMember]

    def perform_create(self, serializer):
        group = Group.objects.get(pk=self.kwargs["id"])
        serializer.save(
            group=group,
            user=self.request.user,
            token=secrets.token_urlsafe(7),
        )

    def get_queryset(self):
        """Filter queryset by group"""

        group = Group.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(group=group)
