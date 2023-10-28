""" Permissions for messenger.groups """


from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsGroupMember(BasePermission):
    """Check if the current user is a member of group of the invite link"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.group.user or request.user in obj.group.members.all()
