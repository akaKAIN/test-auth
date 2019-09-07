from django.urls import path

from validate.views import validate_email, validate_name

app_name = 'validate'

urlpatterns = [
    path('email/', validate_email, name='email'),
    path('name/', validate_name, name='name'),


]
