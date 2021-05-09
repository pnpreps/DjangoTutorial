from django.db import models

# Create your models here.
class contactBooks(models.Model):
	name = models.CharField(max_length=20)
	phone = models.IntegerField()