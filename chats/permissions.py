""" Permissions for messenger.chats """


from rest_framework.permissions import BasePermission


# Create your permissions here
class IsChatParticipant(BasePermission):
    """Allow access only for from_user and to_user"""

    def has_object_permission(self, request, view, obj):
        return request.user in (obj.from_user, obj.to_user)
