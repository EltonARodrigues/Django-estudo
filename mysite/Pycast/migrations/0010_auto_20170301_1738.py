# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-01 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pycast', '0009_auto_20170301_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='/img'),
        ),
    ]
