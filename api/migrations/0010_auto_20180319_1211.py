# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-19 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_promocode_userper_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='promocode',
            name='userper_user',
        ),
        migrations.AddField(
            model_name='promocode',
            name='numberofusers',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]