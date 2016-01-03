from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from producto.models import *

# Create your models here.

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User)
    productos = models.ManyToManyField(Producto)
    fecha = models.DateTimeField(auto_now=True)
    total = models.CharField(max_length=10)

    class Meta:
        db_table = 'venta'
