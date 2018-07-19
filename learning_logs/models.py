from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """A topic the user is learning about"""
    name = models.CharField(max_length=200, default=None)
    prescriber = models.CharField(max_length=200, default=None)
    pharmacy = models.CharField(max_length=200, default=None)
    price = models.FloatField(default=0)
    dose = models.FloatField(default=0)
    dose_units = models.CharField(max_length=100, default=None)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name