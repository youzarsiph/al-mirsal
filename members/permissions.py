""" Permissions for messenger.members """


from rest_framework.permissions import BasePermission
from messenger.members.models import Member


# Create your permissions here.
class IsGroupAdmin(BasePermission):
    """Allow access only to a group admin"""

    def has_object_permission(self, request, view, obj):
        member = Member.objects.get(user=request.user, group=obj.group)
        return request.user == obj.group.user or member.is_admin
