""" URLConf for messenger.msgs """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.urls import actions
from messenger.msgs.views import UserMessagesViewSet
from messenger.reactions.views import MessageReactionsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("messages", UserMessagesViewSet, "message")


urlpatterns = [
    path("", include(router.urls)),
    # Message reactions
    path(
        "<int:id>/reactions/",
        MessageReactionsViewSet.as_view(actions["list_create"]),
    ),
    path(
        "<int:id>/reactions/<int:pk>/",
        MessageReactionsViewSet.as_view(actions["retrieve_update_destroy"]),
    ),
]
