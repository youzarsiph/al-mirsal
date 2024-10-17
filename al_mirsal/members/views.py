""" API endpoints for al_mirsal.members """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from al_mirsal.members.models import Member
from al_mirsal.members.serializers import MemberSerializer
from al_mirsal.mixins import OwnerMixin


# Create your views here.
class MemberViewSet(OwnerMixin, ModelViewSet):
    """Members in groups and channels"""

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["created_at", "updated_at"]
    search_fields = ["user", "channel", "group", "status"]
