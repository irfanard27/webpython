# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-04 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pelajar', '0003_auto_20171104_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelajar',
            name='jenis_kelamin',
            field=models.CharField(choices=[('laki-laki', 'laki-laki'), ('perempuan', 'perempuan')], max_length=100),
        ),
    ]