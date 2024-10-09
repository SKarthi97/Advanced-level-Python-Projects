from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    transaction_amount = models.DecimalField(max_digits=100, decimal_places=2)
    transaction_type = models.ForeignKey('TransactionType', on_delete=models.SET_NULL, blank=True, null=True)
    transaction_method = models.ForeignKey('TransactionMethod', on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.pk}"