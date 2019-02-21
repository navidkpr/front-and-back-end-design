# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-18 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_info', '0003_auto_20190213_2305'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='isOnHome',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='language',
            field=models.CharField(choices=[('Java', 'Java'), ('Javascript', 'JavaScript'), ('Python', 'Python'), ('C++', 'C++'), ('PHP', 'PHP'), ('HTML', 'HTML')], max_length=10),
        ),
    ]
