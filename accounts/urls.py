from django.urls import path, include
from accounts.views import UserLogin, UserLogout, MainView, UserRegisterFormView

app_name = 'accounts'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('registration/', UserRegisterFormView.as_view(), name='reg'),


]
