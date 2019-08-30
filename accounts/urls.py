from django.urls import path
from accounts.views import UserLogin, UserLogout, MainView, UserRegisterFormView, validate_email

app_name = 'accounts'

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('registration/', UserRegisterFormView.as_view(), name='reg'),
    path('validation/', validate_email, name='validate-email')

]
