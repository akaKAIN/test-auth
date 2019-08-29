from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView


class UserLogin(SuccessMessageMixin, LoginView):
    success_message = 'Вы пошли как %(username)s и успешно авторизованны'
    # redirect_authenticated_user = True


class UserLogout(SuccessMessageMixin, LoginRequiredMixin, LogoutView):
    success_message = '%(username)s покинул систему'
    redirect_field_name = '/'


class SendMessage(LoginRequiredMixin, CreateView):
    model = Message

