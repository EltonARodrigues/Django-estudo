# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-02 14:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Pycast', '0011_auto_20170301_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/%Y/%m/%d/'),
            preserve_default=False,
        ),
    ]
