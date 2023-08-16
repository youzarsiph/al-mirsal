""" Views """


from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from messenger.mixins import OwnerMixin
from messenger.views import MemberViewSet, MessageViewSet
from messenger.groups.models import ChatGroup
from messenger.groups.serializers import GroupSerializer


# Create your views here.
User = get_user_model()


class GroupViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete chat groups"""

    queryset = ChatGroup.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = ["name", "description"]
    ordering_fields = []


class UserGroupsViewSet(GroupViewSet):
    """Groups of a particular user"""

    def get_queryset(self):
        """Filter the queryset"""

        # Get the user instance
        user = User.objects.get(pk=self.kwargs["id"])

        # Return filtered queryset
        return super().get_queryset().filter(user=user)


class GroupMembersViewSet(MemberViewSet):
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


class GroupMessagesViewSet(MessageViewSet):
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
