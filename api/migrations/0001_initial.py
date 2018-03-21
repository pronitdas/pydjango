# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-15 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthtokenToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
            ],
            options={
                'db_table': 'authtoken_token',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PushNotificationsApnsdevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.IntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=32, null=True)),
                ('registration_id', models.CharField(max_length=200, unique=True)),
                ('application_id', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'push_notifications_apnsdevice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PushNotificationsGcmdevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.IntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('device_id', models.BigIntegerField(blank=True, null=True)),
                ('registration_id', models.TextField()),
                ('cloud_message_type', models.CharField(max_length=3)),
                ('application_id', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'push_notifications_gcmdevice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PushNotificationsWebpushdevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.IntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('application_id', models.CharField(blank=True, max_length=64, null=True)),
                ('registration_id', models.TextField()),
                ('p256dh', models.CharField(max_length=88)),
                ('auth', models.CharField(max_length=24)),
                ('browser', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'push_notifications_webpushdevice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PushNotificationsWnsdevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.IntegerField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=32, null=True)),
                ('registration_id', models.TextField()),
                ('application_id', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'push_notifications_wnsdevice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trainersession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_created_user_id', models.IntegerField(blank=True, null=True)),
                ('session_duration', models.CharField(blank=True, max_length=45, null=True)),
                ('session_time', models.DateTimeField(blank=True, null=True)),
                ('session_address', models.CharField(blank=True, max_length=300, null=True)),
                ('squad_size', models.CharField(blank=True, max_length=45, null=True)),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(blank=True, max_length=45, null=True)),
                ('level', models.CharField(blank=True, max_length=45, null=True)),
                ('promo_code', models.CharField(blank=True, max_length=45, null=True)),
                ('session_status', models.CharField(blank=True, max_length=45, null=True)),
                ('session_id', models.CharField(blank=True, max_length=45, null=True)),
                ('session_type', models.CharField(blank=True, max_length=45, null=True)),
                ('trainer_id', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'trainersession',
            },
        ),
        migrations.CreateModel(
            name='Trainersignup',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email_id', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('birth_date', models.DateField()),
                ('gender', models.CharField(max_length=45)),
                ('state', models.CharField(max_length=45)),
                ('city', models.CharField(max_length=45)),
                ('postal_code', models.CharField(max_length=45)),
                ('address', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('iscertified', models.BooleanField()),
                ('insured', models.BooleanField()),
                ('working_as_trainer', models.BooleanField()),
                ('device_type', models.CharField(blank=True, max_length=45, null=True)),
                ('device_token', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('trainer_id', models.CharField(blank=True, max_length=45, null=True)),
                ('access_token', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'trainersignup',
            },
        ),
        migrations.CreateModel(
            name='Usersession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('session_type', models.CharField(max_length=45)),
                ('session_duration', models.CharField(max_length=45)),
                ('session_time', models.DateTimeField()),
                ('session_address', models.CharField(max_length=300)),
                ('favorites_trainercode', models.CharField(blank=True, max_length=45, null=True)),
                ('squad_size', models.CharField(blank=True, max_length=45, null=True)),
                ('first_name', models.CharField(blank=True, max_length=45, null=True)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('gender', models.CharField(blank=True, max_length=45, null=True)),
                ('level', models.CharField(blank=True, max_length=45, null=True)),
                ('promo_code', models.CharField(blank=True, max_length=45, null=True)),
                ('session_status', models.CharField(blank=True, max_length=45, null=True)),
                ('session_id', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'usersession',
            },
        ),
        migrations.CreateModel(
            name='Usersignup',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email_id', models.CharField(max_length=45, unique=True)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('age', models.CharField(max_length=45)),
                ('gender', models.CharField(max_length=45)),
                ('level', models.CharField(max_length=45)),
                ('health_issue', models.BooleanField()),
                ('health_condition', models.CharField(blank=True, max_length=45, null=True)),
                ('height', models.CharField(blank=True, max_length=45, null=True)),
                ('weight', models.CharField(blank=True, max_length=45, null=True)),
                ('fitness_goals', models.CharField(blank=True, max_length=45, null=True)),
                ('device_token', models.TextField(blank=True, null=True)),
                ('device_type', models.CharField(blank=True, max_length=45, null=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('access_token', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'usersignup',
            },
        ),
    ]
