from django.contrib import admin
from .models import PersonalWallet, IncomeTransaction, Transaction

admin.site.register(PersonalWallet)
admin.site.register(IncomeTransaction)
admin.site.register(Transaction)