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