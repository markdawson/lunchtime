# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-16 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20160728_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]