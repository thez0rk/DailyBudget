from django.db import models
from django.contrib.auth.models import User
import moneyed
from djmoney.models.fields import MoneyField
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import rrule, MONTHLY, WEEKLY, DAILY, YEARLY
# Create your models here.


class Bill(models.Model):
    DAILY = 'DY'
    WEEKLY = 'WK'
    MONTHLY = 'MT'
    ANNUALLY = 'AN'
    FREQUENCY_CHOICES = (
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (ANNUALLY, 'Annually'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bills')
    name = models.TextField(null=False)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)
    next_due_date = models.DateField(default=start_date, null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    frequency = models.CharField(max_length=2, choices=FREQUENCY_CHOICES, default=MONTHLY)
    deleted = models.BooleanField(null=False, default=False)

    def generate_occurrences(self):
        if self.frequency == self.DAILY:
            print('doin it!')
            for d in rrule(DAILY, count=365, dtstart=self.start_date):
                oc = BillOccurrence(bill=self, billdate=d, amount=self.amount, paid=False)
                oc.save()


class BillOccurrence(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='occurrences')
    billdate = models.DateField()
    amount = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    paid = models.BooleanField(default=False)