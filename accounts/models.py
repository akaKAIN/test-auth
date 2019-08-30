# from django.contrib.auth.models import AbstractUser
# from django.core.mail import send_mail, EmailMessage
# from django.db import models
#
#
# class MainClass(models.Model):
#     """Базовая модель, собержащая общие атрибуты и методы"""
#     def delete(self, *args, **kwargs):
#         self.is_active = False
#         self.save()
#
#
# class Account(AbstractUser, MainClass):
#     """Модель учетной записи пользователей"""
#     def str(self):
#         return f'{self.first_name} {self.last_name}'
#
#     class Meta:
#         verbose_name = 'Учетную запись пользователя'
#         verbose_name_plural = 'Учетные записи пользователей'
#
