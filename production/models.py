from pyexpat import model
from random import choices
from django.db import models

class Pallet(models.Model):
    TURNO = (
        ('1','1º'),
        ('2','2º'),
        ('3','3º')
    )
    Palletqty = models.CharField(max_length=10)
    line = models.CharField(max_length=30)
    operator = models.CharField(max_length=30)
    data_production = models.DateField()
    shift_closed = models.CharField(max_length=1, choices= TURNO, blank=False, null=False)

    def __str__(self):
        return self.line

class Box(models.Model):
    Box_TURNO = (
        ('1','1º'),
        ('2','2º'),
        ('3','3º')
    )
    PRODUCT = (
        ('C','Charger'),
        ('B','Battery'),
    )
    Box_tqty = models.CharField(max_length=10)
    Box_line = models.CharField(max_length=30)
    Box_operator = models.CharField(max_length=30)
    Box_data_production = models.DateField()
    Box_shift_closed = models.CharField(max_length=1, choices= Box_TURNO, blank=False, null=False)
    Box_Product = models.CharField(max_length=1, choices= PRODUCT, blank=False, null=False)

    def __str__(self):
        return self.Box_Product
    