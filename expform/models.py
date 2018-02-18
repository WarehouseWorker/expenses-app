from django.db import models
from django.utils import timezone
from decimal import Decimal

class Spend(models.Model):
    author = models.ForeignKey('auth.User')
    created_data = models.DateTimeField(default=timezone.now)
    customer = models.CharField(max_length=200)
    millage = models.CharField(max_length=7)
    cost = models.DecimalField(Decimal, max_digits=4, decimal_places=2)

    def publish(self):
        self.created_data = timezone.now()
        self.save()

    def __str__(self):
        return self.customer