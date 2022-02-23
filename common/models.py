from email.policy import default
from operator import mod
from django.db import models

# Create your models here.

class Bidding(models.Model):
    user_id = models.IntegerField(default=None)
    item_id = models.IntegerField(default=None)
    bidding_amount = models.FloatField(default=None)

class Item(models.Model):
    name = models.CharField(max_length=50, default='default item')
    bid_price = models.FloatField(default=0.0)
