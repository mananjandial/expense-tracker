from django.db import models
from django.conf import settings


class Budget(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="budgets"
    )

    category = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)

    year = models.IntegerField()
    month = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'category', 'year', 'month')

    def __str__(self):
        return f"{self.user.email} - {self.category} - {self.month}/{self.year}"
