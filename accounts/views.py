"""Вьюхи просмотра страницы отправки сообщений, логина, логаута, регистрации"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView

from accounts.forms import UserCreateForm, MessageForm
from accounts.models import Message


class AbstractMessage:
    """Акстрактный класс хранящий общие параметры для остальных вью с этой моделью"""
    model = Message
    login_url = 'accounts:login'
    paginate_by = 20
    # template_name = 'accounts/registrations.html'


class MainView(LoginRequiredMixin, TemplateView):
    """Класс-вью страницы отправки сообщений. Для авторизованных пользователей."""
    template_name = 'accounts/index.html'
    login_url = 'accounts:login'


class UserLogin(SuccessMessageMixin, LoginView):
    """Класс-вью для авторизации пользователя"""
    success_message = 'Пользователь %(username)s -авторизован.'
    redirect_authenticated_user = True


class UserLogout(LoginRequiredMixin, LogoutView):
    """Класс-вью для 'логаута' пользователя"""
    next_page = 'accounts:main'


class UserRegisterFormView(SuccessMessageMixin, FormView):
    """Класс-вью для регистрации пользователя"""
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:main')
    template_name = 'accounts/registration.html'
    success_message = 'Пользователь %(username)s - успешно зарегистрирован.'

    def form_valid(self, form):
        form.save()
        return super(UserRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(UserRegisterFormView, self).form_invalid(form)


class MessageCreate(LoginRequiredMixin, SuccessMessageMixin, AbstractMessage, CreateView):
    """Класс-вью создания/отправки сообщения пользователя администратору"""
    form_class = MessageForm
    success_message = 'Ваше письмо отправлено администратору'
    success_url = reverse_lazy('accounts:main')
    template_name = 'accounts/message_form.html'
