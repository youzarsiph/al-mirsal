""" Views """


from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from messenger.mixins import OwnerMixin
from messenger.groups.models import ChatGroup
from messenger.groups.serializers import GroupSerializer


# Create your views here.
User = get_user_model()


class GroupViewSet(OwnerMixin, ModelViewSet):
    """ Group ViewSet """

    queryset = ChatGroup.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    search_fields = []
    ordering_fields = []


class UserGroupsViewSet(GroupViewSet):
    """ Groups of a particular user """

    def get_queryset(self):
        """ Filter the queryset """

        # Get the user instance
        user = User.objects.get(pk=self.kwargs['id'])

        # Return filtered queryset
        return super().get_queryset().filter(user=user)
