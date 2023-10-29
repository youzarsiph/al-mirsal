""" API endpoints for messenger.channels """


from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.permissions import IsOwner
from messenger.channels.models import Channel, User
from messenger.channels.serializers import ChannelSerializer
from messenger.members.models import Member


# Create your views here.
class ChannelViewSet(ModelViewSet):
    """Create, read, update and delete channels"""

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        channel = serializer.save(user=self.request.user)
        Member.objects.create(user=self.request.user, channel=channel, admin=True)

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
