from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    vendor = models.CharField(max_length=30)
    desc = models.CharField(max_length=30)
    price = models.FloatField(default=0)
    qty = models.IntegerField(default=0)
    barcode = models.CharField(max_length=30)

    class Meta:
        db_table = 'PRODCUT_INFO'

