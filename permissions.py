""" Custom Permissions """


from rest_framework.permissions import BasePermission


# Create your permissions here
class IsOwner(BasePermission):
    """Allow access only to the owner of the object"""

    def has_object_permission(self, request, view, obj):
        """Check the owner of the object"""

        return request.user == obj.user


class IsUser(BasePermission):
    """Allow access only to the owner of the account"""

    def has_object_permission(self, request, view, obj):
        """Check the owner of the user account"""

        return request.user == obj
