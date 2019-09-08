from django.contrib.auth.models import User
from django.db import models


class MainClass(models.Model):
    """Базовая модель, собержащая общие атрибуты и методы"""

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.save()


class Message(MainClass):
    """Модель сообщения, отправляемого пользователями в адрес 'админа'"""
    mail_from = models.EmailField(
        verbose_name='Отправитель/От кого',
    )
    mail_to = models.EmailField(
        verbose_name='Получатель/Кому',
        default='admin@site.ru',
        blank=True,
    )
    note = models.TextField(verbose_name='Текст сообщения')
    is_read = models.BooleanField(verbose_name='Прочитано', default=False, blank=True)
    mail_date = models.DateTimeField(verbose_name='Дата создания письма', auto_now_add=True)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения пользоватлеей'
        ordering = ('-mail_date', 'mail_from')
