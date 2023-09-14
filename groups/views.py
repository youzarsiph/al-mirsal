""" API endpoints for groups app """


from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from messenger.mixins import OwnerMixin, TokenMixin
from messenger.views import MemberViewSet, MessageViewSet
from messenger.groups.models import ChatGroup
from messenger.groups.serializers import ChatGroupSerializer


# Create your views here.
User = get_user_model()


class ChatGroupViewSet(TokenMixin, OwnerMixin, ModelViewSet):
    """Create, read, update and delete chat groups"""

    queryset = ChatGroup.objects.all()
    serializer_class = ChatGroupSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]

    @action(detail=True)
    def join(self, request, pk):
        """Join the group"""

        # Message
        message: str = f"{request.user} "

        # Group to join
        group = ChatGroup.objects.get(pk=pk)

        if request.user in group.members.all():
            group.members.remove(request.user)
            message += "left the group."
        else:
            group.members.add(request.user)
            message += "joined the group via invite link."

        return Response({"status": message})


class UserChatGroupsViewSet(ChatGroupViewSet):
    """Groups of a user"""

    def get_queryset(self):
        """Filter the queryset"""

        # Get the user instance
        user = User.objects.get(pk=self.kwargs["id"])

        # Return filtered queryset
        return super().get_queryset().filter(user=user)


class ChatGroupMembersViewSet(MemberViewSet):
    """Group members"""

    def perform_create(self, serializer):
        """Creates a member in a group"""

        # Group
        group = ChatGroup.objects.get(pk=self.kwargs["id"])

        # Create the member in group
        serializer.save(user=self.request.user, group=group)

    def get_queryset(self):
        """Filter the queryset by group"""

        # Group
        group = ChatGroup.objects.get(pk=self.kwargs["id"])

        # Return filtered queryset
        return super().get_queryset().filter(group=group)


class ChatGroupMessagesViewSet(MessageViewSet):
    """Group messages"""

    def perform_create(self, serializer):
        """Creates a message in a group"""

        # Group
        group = ChatGroup.objects.get(pk=self.kwargs["id"])

        # Create the message in group
        serializer.save(user=self.request.user, group=group)

    def get_queryset(self):
        """Filter the queryset by group"""

        # Group
        group = ChatGroup.objects.get(pk=self.kwargs["id"])

        # Return filtered queryset
        return super().get_queryset().filter(group=group)
