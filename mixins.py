""" Mixins for messenger """


# Create your mixins here.
class OwnerMixin:
    """Add the user field to a model automatically when creating"""

    def perform_create(self, serializer):
        """Save the model with request.user"""

        serializer.save(user=self.request.user)
