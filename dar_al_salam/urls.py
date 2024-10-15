""" URLConf for dar_al_salam """

from django.urls import path, include
from rest_framework.routers import DefaultRouter


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    # Users
    path("", include(router.urls)),
]
