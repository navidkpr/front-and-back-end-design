# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-18 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info', '0005_auto_20190218_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='isOnProjects',
            field=models.BooleanField(default=0),
        ),
    ]
