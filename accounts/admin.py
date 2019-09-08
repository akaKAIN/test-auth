from django.contrib import admin
from django.contrib.auth.models import User

from accounts.models import Message


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']


class MassageAdmin(admin.ModelAdmin):
    list_display = ['mail_from', 'mail_to',  'mail_date']


# admin.site.register(User, UserAdmin)
admin.site.register(Message, MassageAdmin)
