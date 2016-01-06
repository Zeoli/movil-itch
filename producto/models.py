from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)
    precio = models.CharField(max_length=10)
    imagen = models.FileField(upload_to='products', name='imagen', blank=True)

    class Meta:
        db_table = 'products'

from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Producto)
def photo_post_delete_handler(sender, **kwargs):
    imagen = kwargs['instance']
    storage, path = imagen.imagen.storage, imagen.imagen.path
    storage.delete(path)
