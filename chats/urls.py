""" URLConf for messenger.chats """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.urls import actions
from messenger.chats.views import ChatViewSet
from messenger.msgs.views import ChatMessagesViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("", ChatViewSet, "chat")


urlpatterns = [
    path("", include(router.urls)),
    # Chat messages
    path(
        "<int:id>/messages/",
        ChatMessagesViewSet.as_view(actions["list_create"]),
    ),
    path(
        "<int:id>/messages/<int:pk>/",
        ChatMessagesViewSet.as_view(actions["retrieve_update_destroy"]),
    ),
]
