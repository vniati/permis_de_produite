# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PdP', '0004_auto_20160421_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='dyscritique',
            name='description',
            field=models.TextField(default='SOME STRING', max_length=1400),
        ),
        migrations.AddField(
            model_name='dysstandard',
            name='description',
            field=models.TextField(default='SOME STRING', max_length=1400),
        ),
    ]
