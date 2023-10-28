""" Permissions for messenger """


from rest_framework.permissions import BasePermission


# Create your permissions here.
class IsOwner(BasePermission):
    """Allow access only to the owner of the object"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsUser(BasePermission):
    """Allow access only to the owner of the account"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj


class IsMember(BasePermission):
    """Allow access only to the members of a group or account"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user in obj.members.all()


class IsAdminMember(BasePermission):
    """Allow access to admin members"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or obj.members.get(user=request.user).admin
