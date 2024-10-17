""" API endpoints for al_mirsal.groups """

from django.utils.text import slugify
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_mirsal.groups.models import Group
from al_mirsal.groups.serializers import GroupSerializer
from al_mirsal.mixins import OwnerMixin


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
