# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20170615_0700'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='canpurchase',
            field=models.BooleanField(default=True),
        ),
    ]
