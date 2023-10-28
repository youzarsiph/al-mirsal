""" Permissions for messenger.channels """


from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsChannelMember(BasePermission):
    """Check if the current user is a member of a channel"""

    def has_object_permission(self, request, view, obj):
        return (
            request.user == obj.channel.user
            or request.user in obj.channel.members.all()
        )
