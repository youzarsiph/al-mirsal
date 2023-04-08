""" Mixins """


from rest_framework.permissions import IsAuthenticated
from messenger.permissions import IsOwner


# Create your mixins here.
class OwnerMixin:
    """ Add the user field to a model automatically when creating """

    def perform_create(self, serializer):
        """ Add the user field to a model automatically """

        serializer.save(user=self.request.user)

    def get_permissions(self):
        """ Customize the permissions based on self.action """

        if self.action in ('create', 'list', 'retrieve'):
            permission_classes = self.permission_classes

        else:
            permission_classes = [IsAuthenticated, IsOwner]

        return [permission() for permission in permission_classes]
