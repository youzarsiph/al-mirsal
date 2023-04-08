""" Views """


from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from messenger.mixins import OwnerMixin
from messenger.groups.models import Group, Member, Message
from messenger.groups.serializers import (
    GroupSerializer,
    MemberSerializer,
    MessageSerializer
)


# Create your views here.
User = get_user_model()


class GroupViewSet(OwnerMixin, ModelViewSet):
    """ Group ViewSet """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
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


class UserGroupsViewSet(GroupViewSet):
    """ Groups of a particular user """

    def get_queryset(self):
        """ Filter the queryset """

        # Get the user instance
        user = User.objects.get(pk=self.kwargs['id'])

        # Return filtered queryset
        return super().get_queryset().filter(user=user)


class GroupMembersViewSet(MemberViewSet):
    """ Members of a group """

    def get_queryset(self):
        """ Filter the queryset """

        # Get the group instance
        group = Group.objects.get(pk=self.kwargs['id'])

        # Return filtered queryset
        return super().get_queryset().filter(group=group)


class GroupMessagesViewSet(MessageViewSet):
    """ Messages of a particular group """

    def get_queryset(self):
        """ Filter the queryset """

        # Get the chat instance
        group = Group.objects.get(pk=self.kwargs['id'])

        # Return filtered queryset
        return super().get_queryset().filter(group=group)
