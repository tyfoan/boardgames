# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 11:00
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tictacoe', '0005_auto_20161012_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='move',
            name='x',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='move',
            name='y',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
