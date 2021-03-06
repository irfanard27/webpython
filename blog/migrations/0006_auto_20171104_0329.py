# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-04 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20171030_1423'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('isi', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='artikel',
            name='gambar',
            field=models.FileField(upload_to='static/artikel/gambar/'),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='isi',
            field=redactor.fields.RedactorField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='berita',
            name='isi',
            field=redactor.fields.RedactorField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='gambar',
            field=models.FileField(upload_to='static/event/gambar/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='isi',
            field=redactor.fields.RedactorField(verbose_name=''),
        ),
    ]
