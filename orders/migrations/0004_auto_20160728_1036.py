# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-28 06:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_orderitem_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='comments',
            field=models.CharField(default='', max_length=200, verbose_name='Comments for vendor'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='menu_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu_items', to='menu.MenuItem'),
        ),
    ]
