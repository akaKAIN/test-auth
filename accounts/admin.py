"""Переопределение отображения объектов (Сообщений) в админке"""
from django.contrib import admin
from accounts.models import Message


class MassageAdmin(admin.ModelAdmin):
    """Класс с атрибутами, отображаемыми в админке"""
    list_display = ['mail_from', 'mail_to', 'mail_date']


admin.site.register(Message, MassageAdmin)
