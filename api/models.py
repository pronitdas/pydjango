# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Signup(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_id = models.EmailField(unique=True, max_length=45)
    password = models.CharField(max_length=300)
    age = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    level = models.CharField(max_length=45)
    access_token = models.CharField(max_length=300)
    device_type = models.CharField(max_length=50)
    device_token = models.CharField(max_length=300)
    image = models.FileField(null=True,blank=True)


    class Meta:
        managed = False
        db_table = 'signup'






# Create your models here.
def upload_to(instance, filename):
    return 'user_profile_image/{}/{}'.format(instance.user_id, filename)