from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BankAccount(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bank_name = models.CharField(max_length=100)
    bank_acc_number = models.IntegerField()
    balance = models.DecimalField(max_digits=100, decimal_places=2)

    def __str__(self):
        return f"{self.balance}"
    
class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    transaction_amount = models.DecimalField(max_digits=100, decimal_places=2)
    transaction_type = models.ForeignKey('TransactionType', on_delete=models.SET_NULL, blank=True, null=True)
    transaction_method = models.ForeignKey('TransactionMethod', on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.pk}"

class IncomeTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
          return '%s' % self.amount
    
class PersonalWallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=100, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % (self.balance)
