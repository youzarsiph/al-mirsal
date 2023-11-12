""" Permissions for messenger.subscribers """


from rest_framework.permissions import BasePermission
from messenger.subscribers.models import Subscriber


# Create your permissions here.
class IsChannelAdmin(BasePermission):
    """Allow access only to a channel admin"""

    def has_object_permission(self, request, view, obj):
        subscriber = Subscriber.objects.get(user=request.user, channel=obj.channel)
        return request.user == obj.channel.user or subscriber.is_admin
