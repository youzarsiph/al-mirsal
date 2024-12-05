""" API endpoints for al_mirsal.channel """

from django.utils.text import slugify
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_mirsal.mixins import OwnerMixin
from al_mirsal.channel.models import Channel
from al_mirsal.channel.serializers import ChannelSerializer


# Create your views here.
class ChannelViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete Channels"""

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "slug", "is_private"]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            slug=slugify(serializer.validated_data["slug"]),
        )

    def perform_update(self, serializer):
        serializer.save(slug=slugify(serializer.validated_data["slug"]))

    def get_serializer_class(self):
        if self.action == "join":
            self.serializer_class = Serializer

        return super().get_serializer_class()

    @action(methods=["post"], detail=True)
    def join(self, request: Request, pk: int) -> Response:
        """
        Join a channel
        """

        message: str
        channel: Channel = self.get_object()

        if request.user in channel.subscribers.all():
            channel.subscribers.remove(request.user)
            message = f"You left {channel}!"

        else:
            channel.subscribers.add(request.user)
            message = f"You joined {channel}!"

        return Response(status=status.HTTP_201_CREATED, data={"details": message})
