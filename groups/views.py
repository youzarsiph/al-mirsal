""" API endpoints for messenger.groups """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.groups.models import Group
from messenger.groups.serializers import GroupSerializer
from messenger.members.models import Member


# Create your views here.
class GroupViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete chat groups"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        group = serializer.save(user=self.request.user)
        Member.objects.create(user=self.request.user, group=group, is_admin=True)


class UserGroupsViewSet(GroupViewSet):
    """Groups of a user"""

    def get_queryset(self):
        """Filter the queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
