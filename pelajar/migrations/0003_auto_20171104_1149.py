# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelajar', '0002_auto_20171104_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelajar',
            name='jenis_kelamin',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organisasi',
            name='nama_organisasi',
            field=models.CharField(max_length=100),
        ),
    ]
