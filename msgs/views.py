""" API endpoints for messenger.msgs """


from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.permissions import IsAdminMember, IsOwner
from messenger.channels.models import Channel
from messenger.channels.permissions import IsChannelMember
from messenger.chats.models import Chat
from messenger.chats.permissions import IsChatParticipant
from messenger.groups.models import Group
from messenger.groups.permissions import IsGroupMember
from messenger.msgs.models import Message
from messenger.msgs.serializers import MessageSerializer


# Create your views here.
class MessageViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete messages"""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["text", "photo", "file"]
    ordering_fields = ["created_at"]
    filterset_fields = ["pinned", "starred"]

    @action(detail=True, methods=["post"])
    def pin(self, request, pk):
        """Pin a message"""

        message = self.get_object()

        if message.pinned:
            message.pinned = False
        else:
            message.pinned = True

        message.save()

        return Response(status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]
        elif self.action == "pin":
            self.permission_classes += [IsAdminMember]

        return super().get_permissions()


class ChannelMessagesViewSet(MessageViewSet):
    """Channel messages"""

    permission_classes = [IsAuthenticated, IsChannelMember]

    def perform_create(self, serializer):
        """Creates a message in a channel"""

        channel = Channel.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, channel=channel)

    def get_queryset(self):
        """Filter the queryset by channel"""

        channel = Channel.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(channel=channel)


class ChatMessagesViewSet(MessageViewSet):
    """Chat messages"""

    permission_classes = [IsAuthenticated, IsChatParticipant]

    def perform_create(self, serializer):
        """Creates a message in a chat"""

        chat = Chat.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, chat=chat)

    def get_queryset(self):
        """Filter the queryset by chat"""

        chat = Chat.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(chat=chat)


class GroupMessagesViewSet(MessageViewSet):
    """Group messages"""

    permission_classes = [IsAuthenticated, IsGroupMember]

    def perform_create(self, serializer):
        """Creates a message in a group"""

        group = Group.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, group=group)

    def get_queryset(self):
        """Filter the queryset by group"""

        group = Group.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(group=group)


class UserMessagesViewSet(MessageViewSet):
    """User Messages"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
