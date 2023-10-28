""" URLConf for messenger.forwards """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.forwards.views import UserForwardsViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("forwards", UserForwardsViewSet, "forward")


urlpatterns = [
    path("", include(router.urls)),
]
