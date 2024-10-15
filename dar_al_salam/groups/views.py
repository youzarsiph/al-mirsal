""" API endpoints for dar_al_salam.groups """

from django.utils.text import slugify
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from dar_al_salam.groups.models import Group
from dar_al_salam.groups.serializers import GroupSerializer
from dar_al_salam.mixins import OwnerMixin


# Create your views here.
class GroupViewSet(OwnerMixin, ModelViewSet):
    """Create, read, update and delete chat groups"""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    filterset_fields = ["user", "slug", "is_private"]

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            slug=slugify(serializer.validated_data["name"]),
        )
