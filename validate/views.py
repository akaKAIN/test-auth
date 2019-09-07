from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
import re


def validate_email(request):
    def is_valid(text):
        pattern = r'^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,5}$'
        find_text = re.findall(pattern, text)
        if text in find_text:
            return True

    if request.method == 'POST' and request.is_ajax():
        user_email = request.POST.get('email', None)
        email = {}

        if not user_email:
            email.update({'error': 'Поле "email" не заполнено'})
        elif not is_valid(user_email):
            email.update({'error': 'Данные "email" - неверные'})
        elif User.objects.filter(email=user_email).exists():
            email.update({'error': 'Почтовый ящик занят'})
        else:
            email.update({'answer': 'Почтовый ящик свободен'})
        return JsonResponse(email)


def validate_name(request):
    if request.method == 'GET' and request.is_ajax():
        user_name = request.GET.get('name', None)
        name = {}
        if not user_name:
            name.update({'error': 'Поле "Имя польователя" не заполнено'})
        elif User.objects.filter(username=user_name).exists():
            name.update({'error': 'Даное имя занято, выберите другое'})
        else:
            name.update({'answer': 'Имя пользователя свободено'})
        return JsonResponse(name)