from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from datetime import datetime
from datetime import timedelta

class Topic(models.Model):
    """A topic the user is learning about"""
    name = models.CharField(max_length=200, default=None)
    prescriber = models.CharField(max_length=200, default=None)
    pharmacy = models.CharField(max_length=200, default=None)
    price = models.FloatField()
    dose = models.FloatField()
    dose_units = models.CharField(max_length=100, default=None)
    pill_count = models.IntegerField()
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def expiration_status(self):
        if datetime.now().date() > self.expiration_date:
            return 'danger'
        elif datetime.now().date() > self.expiration_date - timedelta(days=15):
            return 'primary'
        else:
            return 'success'

    @property
    def expiration_text(self):
        if datetime.now().date() > self.expiration_date:
            return 'Expired'
        elif datetime.now().date() > self.expiration_date - timedelta(days=15):
            return 'Expiring'
        else:
            return 'Valid'

    def __str__(self):
        """Return a string representation of the model"""
        return self.name