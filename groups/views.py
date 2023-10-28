""" API endpoints for messenger.groups """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.groups.models import Group, User
from messenger.groups.serializers import GroupSerializer


# Create your views here.
class GroupViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete chat groups"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]


class UserGroupsViewSet(GroupViewSet):
    """Groups of a user"""

    def get_queryset(self):
        """Filter the queryset by user"""

        user = User.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(user=user)
