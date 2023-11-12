""" URLConf for messenger.subscribers """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.subscribers.views import UserSubscribersViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("subscribers", UserSubscribersViewSet, "subscriber")


urlpatterns = [
    path("", include(router.urls)),
]
