""" API endpoints for messenger.links """


import secrets
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.channels.models import Channel
from messenger.groups.models import Group
from messenger.links.models import ChannelLink, GroupLink
from messenger.channels.permissions import IsChannelMember
from messenger.groups.permissions import IsGroupMember
from messenger.links.serializers import ChannelLinkSerializer, GroupLinkSerializer


# Create your views here.
class ChannelLinkViewSet(ModelViewSet):
    """Create, read, update and delete Invite Links for Channels"""

    queryset = ChannelLink.objects.all()
    serializer_class = ChannelLinkSerializer
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


class GroupLinkViewSet(ModelViewSet):
    """Create, read, update and delete Invite Links for Groups"""

    queryset = GroupLink.objects.all()
    serializer_class = GroupLinkSerializer
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
