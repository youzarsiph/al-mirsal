""" Permissions for dar_al_salam """

from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsOwner(BasePermission):
    """Allow access only to the owner of the object"""

    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.user_id


class IsAccountOwner(BasePermission):
    """Allow access only to the owner of the account"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsMember(BasePermission):
    """Allow access only to the members of a group or channel"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user in obj.members.all()


class IsChatOwner(BasePermission):
    """Allow access only to the owner of the chat"""

    def has_object_permission(self, request, view, obj):
        return request.user.id in (obj.from_user_id, obj.to_user_id)
