# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Promocode(models.Model):
    promo_id = models.AutoField(primary_key=True)
    promo_code = models.CharField(max_length=45)
    expiry_date = models.DateTimeField(blank=True, null=True)
    maxuse_peruser = models.IntegerField()

    class Meta:
        db_table = 'promocode'


class PushNotificationsApnsdevice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=32, blank=True, null=True)
    registration_id = models.CharField(unique=True, max_length=200)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    application_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_notifications_apnsdevice'


class PushNotificationsGcmdevice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    device_id = models.BigIntegerField(blank=True, null=True)
    registration_id = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    cloud_message_type = models.CharField(max_length=3)
    application_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_notifications_gcmdevice'


class PushNotificationsWebpushdevice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    application_id = models.CharField(max_length=64, blank=True, null=True)
    registration_id = models.TextField()
    p256dh = models.CharField(max_length=88)
    auth = models.CharField(max_length=24)
    browser = models.CharField(max_length=10)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_notifications_webpushdevice'


class PushNotificationsWnsdevice(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=32, blank=True, null=True)
    registration_id = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    application_id = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'push_notifications_wnsdevice'


class Trainersession(models.Model):
    session_created_user_id = models.IntegerField(blank=True, null=True)
    session_duration = models.CharField(max_length=45, blank=True, null=True)
    session_time = models.DateTimeField(blank=True, null=True)
    session_address = models.CharField(max_length=300, blank=True, null=True)
    squad_size = models.CharField(max_length=45, blank=True, null=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    level = models.CharField(max_length=45, blank=True, null=True)
    promo_code = models.CharField(max_length=45, blank=True, null=True)
    session_status = models.CharField(max_length=45, blank=True, null=True)
    session_id = models.CharField(max_length=45, blank=True, null=True)
    session_type = models.CharField(max_length=45, blank=True, null=True)
    trainer_id = models.CharField(max_length=45, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainersession'


class Trainersignup(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_id = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45, blank=True, null=True)
    birth_date = models.DateField()
    gender = models.CharField(max_length=45)
    state = models.CharField(max_length=45)
    city = models.CharField(max_length=45)
    postal_code = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    iscertified = models.BooleanField()
    insured = models.BooleanField()
    working_as_trainer = models.BooleanField()
    device_type = models.CharField(max_length=45, blank=True, null=True)
    device_token = models.TextField(blank=True, null=True)
    image = models.ImageField()
    trainer_code = models.CharField(max_length=45, blank=True, null=True)
    access_token = models.CharField(max_length=45, blank=True, null=True)
    latitude = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trainersignup'


class Usersession(models.Model):
    user_id = models.IntegerField()
    session_type = models.CharField(max_length=45)
    session_duration = models.CharField(max_length=45)
    session_time = models.DateTimeField()
    session_address = models.CharField(max_length=300)
    favorites_trainercode = models.CharField(max_length=45, blank=True, null=True)
    squad_size = models.CharField(max_length=45, blank=True, null=True)
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    level = models.CharField(max_length=45, blank=True, null=True)
    promo_code = models.CharField(max_length=45, blank=True, null=True)
    session_status = models.CharField(max_length=45, blank=True, null=True)
    session_id = models.CharField(max_length=45)
    latitude = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.CharField(max_length=45, blank=True, null=True)
    price = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usersession'


class Usersignup(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_id = models.CharField(unique=True, max_length=45)
    password = models.CharField(max_length=45, blank=True, null=True)
    age = models.CharField(max_length=45)
    gender = models.CharField(max_length=45)
    level = models.CharField(max_length=45)
    health_issue = models.BooleanField()
    health_condition = models.CharField(max_length=500, blank=True, null=True)
    height = models.CharField(max_length=45, blank=True, null=True)
    weight = models.CharField(max_length=45, blank=True, null=True)
    fitness_goals = models.CharField(max_length=45, blank=True, null=True)
    device_token = models.TextField(blank=True, null=True)
    device_type = models.CharField(max_length=45, blank=True, null=True)
    image = models.ImageField()
    access_token = models.CharField(max_length=45, blank=True, null=True)
    latitude = models.CharField(max_length=45, blank=True, null=True)
    longitude = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usersignup'
