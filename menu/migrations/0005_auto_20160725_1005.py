# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 06:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20160725_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]
