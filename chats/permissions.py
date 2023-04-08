""" Permissions for chats app """


from rest_framework.permissions import BasePermission


# Create your permissions here
class IsChatOwner(BasePermission):
    """ Allow access only to the owner of the object """

    def has_object_permission(self, request, view, obj):
        """ Check the owner of the object """

        return request.user in (obj.from_user, obj.to_user)
