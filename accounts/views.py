from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView, FormView
from accounts.models import Account


class UserLogin(LoginView):
    success_message = 'Вы пошли как %(username)s и успешно авторизованны'
    redirect_authenticated_user = True


class UserLogout(SuccessMessageMixin, LoginRequiredMixin, LogoutView):
    success_message = '%(username)s покинул систему'
    next_page = '/'


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'
    login_url = '/login'


class UserRegisterFormView(FormView):
    # form_class = UserCreateForm
    success_url = '/login'
    template_name = 'accounts/registration.html'
