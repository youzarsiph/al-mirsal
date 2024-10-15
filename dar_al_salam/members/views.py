""" API endpoints for dar_al_salam.members """

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from dar_al_salam.members.models import Member
from dar_al_salam.members.serializers import MemberSerializer
from dar_al_salam.mixins import OwnerMixin


# Create your views here.
class MemberViewSet(OwnerMixin, ModelViewSet):
    """Members in groups and channels"""

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ["created_at", "updated_at"]
    search_fields = ["user", "channel", "group", "status"]
