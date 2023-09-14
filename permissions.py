""" Custom Permissions """


from rest_framework.permissions import SAFE_METHODS, BasePermission


# Create your permissions here
class IsOwner(BasePermission):
    """Allow access only to the owner of the object"""

    def has_object_permission(self, request, view, obj):
        """Check if the current logged in user is the owner of obj"""

        return request.user == obj.user


class IsOwnerOrReadOnly(BasePermission):
    """Allow access only to the owner of the object"""

    def has_object_permission(self, request, view, obj):
        """Check if the current logged in user is the owner of obj"""

        return request.method in SAFE_METHODS or request.user == obj.user


class IsUser(BasePermission):
    """Allow access only to the owner of the account"""

    def has_object_permission(self, request, view, obj):
        """Check if the current logged in user is the owner of the account"""

        return request.method in SAFE_METHODS or request.user == obj


class IsMember(BasePermission):
    """Allow access only to the members of a group or account"""

    def has_object_permission(self, request, view, obj):
        """Check if the current logged in user is a member in the group or account"""

        return request.user in obj.members.all()
