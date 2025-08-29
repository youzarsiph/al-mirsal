"""Views for al_mirsal.ui"""

from secrets import token_urlsafe

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db import IntegrityError
from django.forms import BaseForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django.views import generic
from django_filters.views import FilterView

from al_mirsal.apps.chats.models import Chat
from al_mirsal.ui import mixins
from al_mirsal.ui.forms import UserCreateForm

# Create your views here.
User = get_user_model()


class HomeView(generic.TemplateView):
    """Home page"""

    template_name = "al_mirsal/index.html"


class AboutView(generic.TemplateView):
    """About page"""

    template_name = "al_mirsal/about.html"


class ContactView(generic.TemplateView):
    """Contact page"""

    template_name = "al_mirsal/contact.html"


class ProfileView(LoginRequiredMixin, generic.TemplateView):
    """Profile page"""

    template_name = "registration/profile.html"


class SignupView(SuccessMessageMixin, generic.CreateView):
    """Create a new user"""

    model = User
    form_class = UserCreateForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("al-mirsal:profile")
    success_message = "Your account was created successfully!"


class UserUpdateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    mixins.AccountOwnerMixin,
    generic.UpdateView,
):
    """Update a user"""

    model = User
    template_name = "registration/edit.html"
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("al-mirsal:profile")
    success_message = "Your account was updated successfully!"


class UserDeleteView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    mixins.AccountOwnerMixin,
    generic.DeleteView,
):
    """Delete a user"""

    model = User
    template_name = "registration/delete.html"
    success_url = reverse_lazy("al-mirsal:index")
    success_message = "Your account was deleted successfully!"


# Chats
class ChatCreateView(
    LoginRequiredMixin,
    SuccessMessageMixin,
    generic.CreateView,
):
    """Chat create view"""

    model = Chat
    template_name = "al_mirsal/chats/new.html"
    success_url = reverse_lazy("al-mirsal:chats")
    success_message = _("Chat created successfully.")
    fields = ["model", "title", "description", "role", "is_pinned"]

    def form_valid(self, form: BaseForm) -> HttpResponse:

        chat = form.save(commit=False)
        chat.user = self.request.user

        try:
            chat.slug = slugify(chat.title, allow_unicode=True)
            return super().form_valid(form)

        except IntegrityError:
            chat.slug = slugify(chat.title, allow_unicode=True) + token_urlsafe(6)
            return super().form_valid(form)


class ChatListView(LoginRequiredMixin, FilterView, generic.ListView):
    """Chat list"""

    model = Chat
    paginate_by = 50
    context_object_name = "chats"
    template_name = "al_mirsal/chats/list.html"
    filterset_fields = ["model", "is_pinned"]


class ChatDetailView(LoginRequiredMixin, mixins.OwnerFilterMixin, generic.DetailView):
    """Chat details"""

    model = Chat
    template_name = "al_mirsal/chats/id.html"


class ChatUpdateView(
    LoginRequiredMixin,
    mixins.OwnerFilterMixin,
    SuccessMessageMixin,
    generic.UpdateView,
):
    """Chat update view"""

    model = Chat
    template_name = "al_mirsal/chats/new.html"
    success_url = reverse_lazy("al-mirsal:chats")
    success_message = _("Chat updated successfully.")
    fields = ["model", "title", "description", "role", "is_pinned"]


class ChatDeleteView(
    LoginRequiredMixin,
    mixins.OwnerFilterMixin,
    SuccessMessageMixin,
    generic.DeleteView,
):
    """Chat update view"""

    model = Chat
    template_name = "al_mirsal/chats/new.html"
    success_url = reverse_lazy("al-mirsal:chats")
    success_message = _("Chat deleted successfully.")
