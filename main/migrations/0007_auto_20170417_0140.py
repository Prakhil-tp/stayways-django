# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 20:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170417_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.IntegerField(default=0.0, verbose_name='Price'),
        ),
    ]
