# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 10:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_product_canpurchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rate',
            field=models.IntegerField(default=4),
        ),
    ]
