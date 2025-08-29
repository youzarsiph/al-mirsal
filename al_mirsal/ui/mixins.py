"""Generic View Mixins for al_mirsal.ui"""

from typing import Optional

from django.contrib.auth.mixins import UserPassesTestMixin
from django.forms import BaseModelForm
from django.http import HttpResponse


# Create your mixins here.
class AdminUserMixin(UserPassesTestMixin):
    """Check if the user is an admin"""

    def test_func(self) -> Optional[bool]:
        return self.request.user.is_staff


class AccountOwnerMixin(UserPassesTestMixin):
    """Check if the user is owner of the account"""

    def test_func(self) -> Optional[bool]:
        return self.request.user == self.get_object()


class ObjectOwnerMixin:
    """Adds the owner automatically"""

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        """Add the owner of the object automatically"""

        obj = form.save(commit=False)
        obj.user_id = self.request.user.id

        return super().form_valid(form)


class OwnerFilterMixin:
    """Filters queryset by owner"""

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
