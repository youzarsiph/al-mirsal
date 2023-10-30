""" URLConf for messenger.links """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.links.views import UserLinksViewSet


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)
router.register("links", UserLinksViewSet, "link")

urlpatterns = [
    path("", include(router.urls)),
]
