# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='status',
            field=models.BooleanField(default=1),
        ),
    ]
