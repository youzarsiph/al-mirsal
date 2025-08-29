"""URL Configuration for al_mirsal.api"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from al_mirsal.api import viewsets

# Create your URLConf here.
router = DefaultRouter()
router.register("channels", viewsets.ChannelViewSet, "channel")
router.register("chats", viewsets.ChatViewSet, "chat")
router.register("groups", viewsets.GroupViewSet, "group")
router.register("members", viewsets.MemberViewSet, "member")
router.register("messages", viewsets.MessageViewSet, "message")
router.register("users", viewsets.UserViewSet, "user")


urlpatterns = [
    path("", include(router.urls)),
]
