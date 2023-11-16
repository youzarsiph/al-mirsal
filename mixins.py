""" Mixins for messenger """


from messenger.permissions import IsOwner


# Create your mixins here.
class OwnerMixin:
    """Add the user field to a model automatically when creating"""

    def perform_create(self, serializer):
        """Save the model with request.user"""

        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ["update", "partial_update", "destroy"]:
            self.permission_classes += [IsOwner]

        return super().get_permissions()
