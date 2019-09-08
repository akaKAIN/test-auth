"""Форма для регистрации пользователя (дополненая полем email базовая форма)"""
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from accounts.models import Message
import requests
import json


class UserCreateForm(UserCreationForm):
    """Класс-форма для регистрации пользователя"""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class MessageForm(forms.ModelForm):
    """Класс-форма для модели Сообщений, отправляемым пользователем администратору"""

    class Meta:
        model = Message
        fields = ('mail_from', 'note')

    def clean_note(self):
        """Функция берет данные из отправленой формы и дополняет поле note из внешнего источника"""
        email = self.cleaned_data['mail_from']
        note = self.cleaned_data['note']
        return note + self.check_outside(email)

    @staticmethod
    def check_outside(email):
        """Функиця поиска совпадений во внешнем источнике. Если есть совпадение почты в удаленном массиве,
        возвращает все данные о пользователе, чьи данные совпали"""
        url = 'http://jsonplaceholder.typicode.com/users'
        check_request = requests.get(url)
        users_list = json.loads(check_request.text)
        for user in users_list:
            if email in user.values():
                return '\n\n' + json.dumps(user)
        return ''
