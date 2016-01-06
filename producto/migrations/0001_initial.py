# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=10)),
                ('imagen', models.FileField(blank=True, upload_to='products')),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
