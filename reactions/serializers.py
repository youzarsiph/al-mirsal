""" Serializers for messenger.reactions """


from rest_framework.serializers import ModelSerializer
from messenger.reactions.models import Reaction


# Create your serializers here.
class ReactionSerializer(ModelSerializer):
    """Reaction Serializer"""

    class Meta:
        """Meta data"""

        model = Reaction
        fields = ["id", "url", "value", "created_at", "updated_at"]
