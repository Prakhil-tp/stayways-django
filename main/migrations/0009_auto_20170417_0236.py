# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 21:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20170417_0218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='user_id',
            new_name='user',
        ),
    ]
