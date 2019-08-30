from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from accounts.forms import UserCreateForm


class MainView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/index.html'
    login_url = 'accounts:login'

    def get(self, request, *args):
        context = {}
        if request.user.is_authenticated:
            users = User.objects.all()
            context.update({
                'users': users,
            })
        return render(request, self.template_name, context)


class UserLogin(SuccessMessageMixin, LoginView):
    success_message = 'Пользователь %(username)s -авторизован.'
    redirect_authenticated_user = True


class UserLogout(LoginRequiredMixin, LogoutView):
    next_page = 'accounts:main'


class UserRegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = '/'
    template_name = 'accounts/registration.html'

    def form_valid(self, form):
        form.save()
        return super(UserRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(UserRegisterFormView, self).form_invalid(form)


def validate_email(request):
    if request.method == 'POST':
        data = {}
        email = request.POST.get('email')
        is_taken = User.objects.filter(email=email).exists()
        if request.is_ajax():
            if is_taken:
                data = {'is_taken': 'Пользователь с такой почтой уже существует'}
            else:
                data = {'ok': 'Почтовый ящик свободен'}
        return JsonResponse(data)
