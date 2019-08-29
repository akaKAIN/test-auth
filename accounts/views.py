from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render


# Create your views here.

class UserLogin(SuccessMessageMixin, LoginView):
    success_message = 'Вы пошли как %(username)s и успешно авторизованны'
    redirect_authenticated_user = True

