""" URLConf for messenger.members """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.members.views import UserMembersViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("members", UserMembersViewSet, "member")


urlpatterns = [
    path("", include(router.urls)),
]
