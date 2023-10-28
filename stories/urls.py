""" URLConf for messenger.stories """


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from messenger.stories import views


# Create your URLConf here.
router = DefaultRouter(trailing_slash=False)


urlpatterns = [
    path("", include(router.urls)),
]
