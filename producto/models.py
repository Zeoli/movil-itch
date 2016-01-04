from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)
    precio = models.CharField(max_length=10)

    class Meta:
        db_table = 'producto'
