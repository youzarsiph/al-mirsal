""" URLConf for messenger.msgs """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.msgs.views import UserMessagesViewSet
from messenger.reactions.views import MessageReactionsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("messages", UserMessagesViewSet, "message")


sub_router = DefaultRouter()
sub_router.register("reactions", MessageReactionsViewSet, "reaction")


urlpatterns = [
    path("", include(router.urls)),
    # Message reactions
    path("messages/<int:id>/", include(sub_router.urls)),
]
