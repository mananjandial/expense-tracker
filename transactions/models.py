from django.db import models
from django.conf import settings


class Transaction(models.Model):

    class TransactionType(models.TextChoices):
        INCOME = "income", "Income"
        EXPENSE = "expense", "Expense"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="transactions"
    )

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(
        max_length=10,
        choices=TransactionType.choices
    )

    category = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['date']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return f"{self.user.email} - {self.type} - {self.amount}"