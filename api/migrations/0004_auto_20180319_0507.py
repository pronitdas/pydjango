# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 05:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180316_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainersession',
            name='price',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='usersession',
            name='price',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
