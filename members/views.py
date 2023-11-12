""" API endpoints for messenger.members """


from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.permissions import IsOwner
from messenger.groups.models import Group
from messenger.members.models import Member
from messenger.members.serializers import MemberSerializer
from messenger.members.permissions import IsGroupAdmin


# Create your views here.
class MemberViewSet(OwnerMixin, ModelViewSet):
    """Members in groups and channels"""

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user__username", "user__first_name", "user__last_name"]

    @action(detail=True, methods=["post"])
    def ban(self, request, pk):
        """Ban a member"""

        member = self.get_object()

        if member.is_banned:
            member.is_banned = False
        else:
            member.is_banned = True

        member.save()

        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def admin(self, request, pk):
        """Make a member admin"""

        member = self.get_object()

        if member.is_admin:
            member.is_admin = False
        else:
            member.is_admin = True

        member.save()

        return Response(status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()


class UserMembersViewSet(MemberViewSet):
    """User Members"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)


class GroupMembersViewSet(MemberViewSet):
    """Group members"""

    def get_permissions(self):
        if self.action in ["ban", "admin"]:
            self.permission_classes += [IsGroupAdmin]

        return super().get_permissions()

    def perform_create(self, serializer):
        """Creates a member in a group"""

        group = Group.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, group=group)

    def get_queryset(self):
        """Filter the queryset by group"""

        group = Group.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(group=group)
