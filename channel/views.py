""" Views for channels app """


from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from messenger.mixins import OwnerMixin
from messenger.channel.models import Channel, Member, Message
from messenger.channel.serializers import (
    ChannelSerializer,
    MemberSerializer,
    MessageSerializer
)


# Create your views here.
User = get_user_model()


class ChannelViewSet(OwnerMixin, ModelViewSet):
    """ Channel ViewSet """

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = []
    ordering_fields = []


class MemberViewSet(OwnerMixin, ModelViewSet):
    """ Member ViewSet """

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = []
    ordering_fields = []


class MessageViewSet(OwnerMixin, ModelViewSet):
    """ Message ViewSet """

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = []
    ordering_fields = []


class UserChannelsViewSet(ChannelViewSet):
    """ Channels of a user """

    def get_queryset(self):
        """ Filter the queryset """

        # Get the user instance
        user = User.objects.get(pk=self.kwargs['id'])

        # Return filtered queryset
        return super().get_queryset().filter(user=user)


class ChannelMembersViewSet(MemberViewSet):
    """ Members of a channel """

    def get_queryset(self):
        """ Filter the queryset """

        # Get the channel instance
        channel = Channel.objects.get(pk=self.kwargs['id'])

        # Return filtered queryset
        return super().get_queryset().filter(channel=channel)


class ChannelMessagesViewSet(MessageViewSet):
    """ Messages of a channel """

    def get_queryset(self):
        """ Filter the queryset """

        # Get the channel instance
        channel = Channel.objects.get(pk=self.kwargs['id'])

        # Return filtered queryset
        return super().get_queryset().filter(channel=channel)
