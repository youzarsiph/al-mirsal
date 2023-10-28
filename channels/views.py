""" API endpoints for messenger.channels """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.permissions import IsOwner
from messenger.channels.models import Channel, User
from messenger.channels.serializers import ChannelSerializer


# Create your views here.
class ChannelViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete channels"""

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()


class UserChannelsViewSet(ChannelViewSet):
    """Channels of a user"""

    def get_queryset(self):
        """Filter the queryset by user"""

        user = User.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(user=user)
