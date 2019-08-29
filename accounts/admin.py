from django.contrib import admin
from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']


admin.site.register(Account, AccountAdmin)
