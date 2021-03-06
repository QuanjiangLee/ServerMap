# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myServerMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostName', models.CharField(max_length=30)),
                ('IPAddress', models.GenericIPAddressField()),
                ('hostUrl', models.URLField()),
                ('hostPort', models.IntegerField()),
                ('createTime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-createTime'],
            },
        ),
    ]
