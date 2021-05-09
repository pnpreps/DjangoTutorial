import expence
from django.db import models

# Create your models here.
class expences(models.Model):
    expence = models.CharField(max_length=30)
    price = models.IntegerField()


class inibal(models.Model):
    inibalance = models.IntegerField()