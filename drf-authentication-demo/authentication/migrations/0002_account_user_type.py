# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='user_type',
            field=models.CharField(choices=[(b'SU', b'Super User'), (b'A', b'User Type A'), (b'B', b'User Type B'), (b'C', b'User Type C')], default=b'C', max_length=2),
        ),
    ]