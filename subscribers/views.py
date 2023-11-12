""" API endpoints for messenger.subscribers """


from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from messenger.mixins import OwnerMixin
from messenger.permissions import IsOwner
from messenger.channels.models import Channel
from messenger.subscribers.models import Subscriber
from messenger.subscribers.serializers import SubscriberSerializer
from messenger.subscribers.permissions import IsChannelAdmin


# Create your views here.
class SubscriberViewSet(OwnerMixin, ModelViewSet):
    """Channel Subscribers"""

    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["user__username", "user__first_name", "user__last_name"]

    @action(detail=True, methods=["post"])
    def ban(self, request, pk):
        """Ban a subscriber"""

        subscriber = self.get_object()

        if subscriber.is_banned:
            subscriber.is_banned = False
        else:
            subscriber.is_banned = True

        subscriber.save()

        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["post"])
    def admin(self, request, pk):
        """Make a subscriber admin"""

        subscriber = self.get_object()

        if subscriber.is_admin:
            subscriber.is_admin = False
        else:
            subscriber.is_admin = True

        subscriber.save()

        return Response(status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()


class ChannelSubscribersViewSet(SubscriberViewSet):
    """Channel subscribers"""

    def get_permissions(self):
        if self.action in ["ban", "admin"]:
            self.permission_classes += [IsChannelAdmin]

        return super().get_permissions()

    def perform_create(self, serializer):
        """Creates a subscriber in a channel"""

        channel = Channel.objects.get(pk=self.kwargs["id"])
        serializer.save(user=self.request.user, channel=channel)

    def get_queryset(self):
        """Filter the queryset by channel"""

        channel = Channel.objects.get(pk=self.kwargs["id"])
        return super().get_queryset().filter(channel=channel)


class UserSubscribersViewSet(SubscriberViewSet):
    """User Subscribers"""

    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """Filter queryset by user"""

        return super().get_queryset().filter(user=self.request.user)
