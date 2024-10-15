""" API endpoints for dar_al_salam.channels """

from django.utils.text import slugify
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from dar_al_salam.mixins import OwnerMixin
from dar_al_salam.channels.models import Channel
from dar_al_salam.channels.serializers import ChannelSerializer


# Create your views here.
class ChannelViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete channels"""

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "slug", "is_private"]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            slug=slugify(serializer.validated_data["name"]),
        )
