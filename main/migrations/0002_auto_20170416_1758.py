# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 12:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='avgrating',
            field=models.IntegerField(null=True, verbose_name='Average Rating'),
        ),
    ]
