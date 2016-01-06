from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, blank=False)
    imagen = models.FileField(upload_to='users', null=True)
    numero = models.CharField(max_length=10)
    Calle = models.CharField(max_length=60)
    Colonia = models.CharField(max_length=60)
    Municipio = models.CharField(max_length=20)
    Estado = models.CharField(max_length=20)
    Ciudad = models.CharField(max_length=20)
    Pais = models.CharField(max_length=60)

    class Meta:
        db_table = 'perfiles'

from django.db.models.signals import post_delete
from django.dispatch import receiver

@receiver(post_delete, sender=Profile)
def photo_post_delete_handler(sender, **kwargs):
    imagen = kwargs['instance']
    storage, path = imagen.imagen.storage, imagen.imagen.path
    storage.delete(path)
